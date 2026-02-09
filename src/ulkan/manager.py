import shutil
from pathlib import Path
from typing import List

from .generator import get_package_path, copy_resource_file
from .styles import console

REGISTRY_PKG = "ulkan.registry"


def list_assets(asset_type: str) -> List[str]:
    """Lists available assets of a given type from the registry.

    Args:
        asset_type: One of 'skills', 'workflows', 'rules', 'tools'.

    Returns:
        List of asset names.
    """
    registry_root = get_package_path(REGISTRY_PKG)
    asset_dir = registry_root / asset_type

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


def search_assets(query: str) -> List[str]:
    """Searches for assets matching the query.

    Args:
        query: Search term.

    Returns:
        List of matching assets in format 'type/name'.
    """
    results = []
    for asset_type in ["skills", "workflows", "rules", "tools"]:
        items = list_assets(asset_type)
        for item in items:
            if query.lower() in item.lower():
                # Singularize type for display/add command
                singular_type = asset_type.rstrip("s")
                results.append(f"{singular_type}/{item}")

    return sorted(results)


def add_asset(asset_type: str, name: str, base_path: Path) -> bool:
    """Adds an asset from the registry to the project.

    Args:
        asset_type: One of 'skill', 'workflow', 'rule', 'tool'. (Singular)
        name: Name of the asset (e.g. 'feat', 'scripts/my-script.py').
        base_path: Project root.

    Returns:
        True if successful.
    """
    registry_root = get_package_path(REGISTRY_PKG)
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
    src_root = registry_root / folder_name
    dest_root = agent_dir / folder_name

    if asset_type == "skill":
        src_path = src_root / name
        dest_path = dest_root / name

        if not src_path.exists():
            console.print(f"[error]Skill '{name}' not found in registry.[/error]")
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
                f"[error]{asset_type.capitalize()} '{name}' not found in registry.[/error]"
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
            console.print(f"[error]Tool '{name}' not found in registry.[/error]")
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
