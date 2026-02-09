import shutil
from pathlib import Path
from typing import List

from .generator import get_package_path, copy_resource_file
from .styles import console

BLUEPRINTS_PKG = "ulkan.blueprints"


def list_assets(asset_type: str) -> List[str]:
    """Lists available assets of a given type from the blueprints.

    Args:
        asset_type: One of 'skills', 'workflows', 'rules', 'tools'.

    Returns:
        List of asset names.
    """
    blueprints_root = get_package_path(BLUEPRINTS_PKG)
    asset_dir = blueprints_root / asset_type

    if not asset_dir.exists():
        return []

    assets = []

    if asset_type == "tools":
        # Tools have categories: tools/scripts/name.py, tools/mcp/name
        for category in asset_dir.iterdir():
            if category.is_dir():
                for item in category.iterdir():
                    if item.is_file() or item.is_dir():  # script or mcp folder
                        assets.append(f"{category.name}/{item.name}")
    else:
        # Skills are dirs, Workflows/Rules are .md files
        for item in asset_dir.iterdir():
            if asset_type == "skills" and item.is_dir():
                assets.append(item.name)
            elif (
                asset_type in ["workflows", "rules"]
                and item.suffix == ".md"
                and item.name != "README.md"
            ):
                assets.append(item.stem)  # 'feat.md' -> 'feat'

    return sorted(assets)


import httpx
from rich.console import Console

SKYLL_API_URL = "https://api.skyll.app/search"


def search_assets(query: str, limit: int = 50, sort_by: str = None) -> List[dict]:
    """Searches for assets using the Skyll API.

    Args:
        query: Search term.
        limit: Number of results to return (default 50).
        sort_by: Optional sorting criteria ('installs' or 'relevance').
                 Note: API sorts by relevance by default. 'installs' is done client-side.

    Returns:
        List of dicts with keys: name, description, install_count, score, source.
    """
    try:
        response = httpx.get(
            SKYLL_API_URL, params={"q": query, "limit": limit}, timeout=10.0
        )
        response.raise_for_status()
        data = response.json()

        # Determine where the skills list is (top-level or inside payload)
        # Based on user info: { "query": ..., "count": ..., "skills": [...] }
        skills = data.get("skills", [])
        if not skills and "payload" in data:
            skills = data["payload"].get("skills", [])

        results = []
        for item in skills:
            # Extract description from content (first line or truncated)
            content = item.get("content", "")
            description = (
                content.split("\n")[0][:100] + "..." if content else "No description"
            )

            # If metadata exists, check if it has description
            if "metadata" in item and isinstance(item["metadata"], dict):
                meta = item["metadata"]
                if "description" in meta:
                    description = meta["description"]

            results.append(
                {
                    "name": item.get("title", "Unknown"),
                    "description": description,
                    "install_count": item.get("install_count", 0),
                    "score": item.get("relevance_score", 0),
                    "source": "skyll",  # Marker to know source
                }
            )

        # Client-side sorting if requested
        if sort_by == "installs":
            results.sort(key=lambda x: x["install_count"], reverse=True)
        # Relevance is default from API, but we can enforce it if needed
        elif sort_by == "relevance":
            results.sort(key=lambda x: x["score"], reverse=True)

        return results

    except Exception as e:
        console.print(f"[error]Failed to search Skyll API: {e}[/error]")
        return []


def install_skill_from_api(name: str, base_path: Path) -> bool:
    """Installs a skill from the Skyll API.

    Args:
        name: Name of the skill to install.
        base_path: Project root.

    Returns:
        True if successful.
    """
    console.print(f"[info]Searching Skyll API for skill '{name}'...[/info]")

    # Search for the skill
    results = search_assets(name, limit=1)

    if not results:
        return False

    skill_data = results[0]

    # Verify if it's a reasonable match?
    # For now, we trust the top result if the user is asking for it.
    # But we might want to warn if the name is very different.
    api_title = skill_data["name"]
    console.print(f"[info]Found: {api_title}[/info]")

    # We need the full content. The search result MIGHT have it in 'content',
    # but let's be sure. The search_assets implementation extracts 'content'.
    # However, 'search_assets' returns a simplified dict.
    # 'search_assets' currently truncates description.
    # We need to fetch the FULL content.
    # The 'search' endpoint returns full content in 'content' field as per user check.
    # BUT my 'search_assets' function returns a constructed dict with truncated description.
    # I should modify 'search_assets' OR make a direct call here to get the raw data.
    # Making a direct call here is safer to get the full content without altering search_assets signature too much.

    try:
        response = httpx.get(
            SKYLL_API_URL, params={"q": name, "limit": 1}, timeout=10.0
        )
        response.raise_for_status()
        data = response.json()
        skills = data.get("skills", [])
        if not skills and "payload" in data:
            skills = data["payload"].get("skills", [])

        if not skills:
            return False

        target_skill = skills[0]
        content = target_skill.get("content", "")

        if not content:
            console.print("[error]Skill content is empty![/error]")
            return False

        # Install logic
        agent_dir = base_path / ".agent"
        skills_dir = agent_dir / "skills"

        # Use the requested name for the folder to match user expectation/args
        # sanitize name just in case?
        safe_name = name.replace(" ", "-").replace("/", "-").lower()
        target_dir = skills_dir / safe_name

        if target_dir.exists():
            console.print(
                f"[warning]Skill '{safe_name}' already exists. Overwriting...[/warning]"
            )
        else:
            target_dir.mkdir(parents=True, exist_ok=True)

        # Prepare valid YAML frontmatter
        # We try to fill as much as we can from API data
        title = target_skill.get("title", name)
        # Description: clean up newlines for YAML block scalar if needed, or just use string
        # user requested: description: > ...
        raw_desc = target_skill.get("description", "")
        if not raw_desc and "metadata" in target_skill:
            raw_desc = target_skill["metadata"].get("description", "")
        if not raw_desc:
            # Try to take first paragraph of content
            raw_desc = content.split("\n\n")[0].strip()

        # Clean description for YAML (basic)
        description = raw_desc.replace('"', '\\"')

        # Author
        author = "Unknown"
        if "metadata" in target_skill:
            author = target_skill["metadata"].get("author", "Unknown")

        # License
        license_ = "Apache-2.0"  # Default as requested, or fetch if available
        if "metadata" in target_skill:
            license_ = target_skill["metadata"].get("license", "Apache-2.0")

        # Construct Frontmatter
        frontmatter = f"""---
name: {safe_name}
description: >
  {description}
trigger: "User asks for {title} or related concepts"
license: {license_}
metadata:
  author: {author}
  agent: universal
  version: "1.0"
  scope: [root]
  auto_invoke: "When user specifically requests {title} features"
allowed-tools: *
---

"""

        # Write SKILL.md with frontmatter prepended
        skill_file = target_dir / "SKILL.md"
        final_content = frontmatter + content
        skill_file.write_text(final_content, encoding="utf-8")

        # NO metadata.json creation (as per user request "envés del metadata") is implicitly done by removing that block.

        console.print(
            f"[success]Installed skill '{safe_name}' from Skyll API![/success]"
        )
        return True

    except Exception as e:
        console.print(f"[error]Failed to install from API: {e}[/error]")
        return False


def add_asset(asset_type: str, name: str, base_path: Path) -> bool:
    """Adds an asset from the blueprints to the project.

    Args:
        asset_type: One of 'skill', 'workflow', 'rule', 'tool'. (Singular)
        name: Name of the asset (e.g. 'feat', 'scripts/my-script.py').
        base_path: Project root.

    Returns:
        True if successful.
    """
    blueprints_root = get_package_path(BLUEPRINTS_PKG)
    agent_dir = base_path / ".agent"

    # Map singular command arg to plural folder name
    type_map = {
        "skill": "skills",
        "workflow": "workflows",
        "rule": "rules",
        "tool": "tools",
    }

    if asset_type not in type_map:
        console.print(f"[error]Unknown asset type: {asset_type}[/error]")
        return False

    folder_name = type_map[asset_type]
    src_root = blueprints_root / folder_name
    dest_root = agent_dir / folder_name

    # PRIORITY: Check API for skills first (or if local fails? User said "Always search in Skyll")
    # Implication: Try API first. If found, good. If not, try local.
    if asset_type == "skill":
        if install_skill_from_api(name, base_path):
            return True
        # If API failed or yielded no results, fall through to local check
        console.print(
            "[info]Skill not found in API or API failed. Checking local registry...[/info]"
        )

    if asset_type == "skill":
        src_path = src_root / name
        dest_path = dest_root / name

        if not src_path.exists():
            console.print(f"[error]Skill '{name}' not found in blueprints.[/error]")
            return False

        # recursive copy
        for src_file in src_path.rglob("*"):
            if src_file.is_file():
                rel_path = src_file.relative_to(src_path)
                copy_resource_file(src_file, dest_path / rel_path, base_path)
        return True

    elif asset_type in ["workflow", "rule"]:
        # These are simple markdown files
        filename = f"{name}.md"
        src_path = src_root / filename
        dest_path = dest_root / filename

        if not src_path.exists():
            console.print(
                f"[error]{asset_type.capitalize()} '{name}' not found in blueprints.[/error]"
            )
            return False

        return copy_resource_file(src_path, dest_path, base_path)

    elif asset_type == "tool":
        # Name is expected to be 'category/filename'
        parts = name.split("/")
        if len(parts) < 2:
            console.print(
                f"[error]Tool name must be in format 'category/name' (e.g. scripts/myscript.py)[/error]"
            )
            return False

        src_path = src_root / name
        dest_path = dest_root / name

        if not src_path.exists():
            console.print(f"[error]Tool '{name}' not found in blueprints.[/error]")
            return False

        if src_path.is_dir():
            # Recursive copy for directory-based tools (like MCP servers)
            for src_file in src_path.rglob("*"):
                if src_file.is_file():
                    rel_path = src_file.relative_to(src_path)
                    copy_resource_file(src_file, dest_path / rel_path, base_path)
            return True
        else:
            return copy_resource_file(src_path, dest_path, base_path)

    return False
