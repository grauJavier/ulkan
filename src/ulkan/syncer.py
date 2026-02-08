"""
Syncs AGENTS.md with current skills, rules, workflows, and tools.
"""

import os
import re
from pathlib import Path

from .styles import console, print_error, print_step, print_success

AGENTS_FILE = "AGENTS.md"
BASE_DIR = ".agent"


def parse_frontmatter(filepath: Path) -> tuple[str, str, str | None]:
    """Parse frontmatter from a markdown file.

    Returns:
        tuple[name, trigger, description]
    """
    try:
        content = filepath.read_text()
    except Exception:
        return filepath.stem, "Error reading file", None

    name_match = re.search(r"name:\s*(.+)", content)
    trigger_match = re.search(r'trigger:\s*["\']?([^"\']+)["\']?', content)
    desc_match = re.search(r"description:\s*>\s*(.+?)(\n\w|$)", content, re.DOTALL)
    if not desc_match:
        desc_match = re.search(r"description:\s*(.+)", content)

    name = (
        name_match.group(1).strip()
        if name_match
        else (filepath.parent.name if filepath.name == "SKILL.md" else filepath.stem)
    )
    trigger = trigger_match.group(1).strip() if trigger_match else "See file"

    desc = "No description."
    if desc_match:
        desc = desc_match.group(1).strip().replace("\n", " ")
        if len(desc) > 100:
            desc = desc[:97] + "..."

    return name, trigger, desc


def get_skills(root: Path) -> list[str]:
    skills_dir = root / BASE_DIR / "skills"
    rows = []
    if skills_dir.exists():
        for f in skills_dir.glob("*/SKILL.md"):
            name, trigger, desc = parse_frontmatter(f)
            rows.append(f'| `{name}` | "{trigger}" | {desc} |')
    return sorted(rows)


def get_rules(root: Path) -> list[str]:
    rules_dir = root / BASE_DIR / "rules"
    rows = []
    if rules_dir.exists():
        for f in rules_dir.glob("*.md"):
            if f.name == "README.md":
                continue
            name, trigger, desc = parse_frontmatter(f)
            rows.append(f'| `{name}` | "{trigger}" | {desc} |')
    return sorted(rows)


def get_workflows(root: Path) -> list[str]:
    workflows_dir = root / BASE_DIR / "workflows"
    rows = []
    if workflows_dir.exists():
        for f in workflows_dir.glob("*.md"):
            if f.name == "README.md":
                continue
            name, trigger, desc = parse_frontmatter(f)
            # Ensure workflow name starts with /
            if not name.startswith("/"):
                name = f"/{name}"
            rows.append(f'| `{name}` | "{trigger}" | {desc} |')
    return sorted(rows)


def get_tools(root: Path) -> list[str]:
    tools_dir = root / BASE_DIR / "tools" / "scripts"
    rows = []
    if tools_dir.exists():
        for f in tools_dir.glob("*"):
            if f.suffix in [".py", ".sh"]:
                name = f.name
                desc = "Script utility."
                try:
                    content = f.read_text()[:500]
                    doc_match = re.search(r'("""|\'\'\')([\s\S]*?)\1', content)
                    if doc_match:
                        desc = doc_match.group(2).strip().replace("\n", " ")[:100]
                except Exception:
                    pass
                rows.append(f"| `{name}` | Script | {desc} |")
    return sorted(rows)


def update_table(content: str, header: str, rows: list[str]) -> str:
    if not rows:
        return content
    # Regex to find the markdown table under a specific header
    pattern = re.compile(
        rf"(### {re.escape(header)}[\s\S]*?\| :--- \|\n)([\s\S]*?)(?=\n\n|\n#)",
        re.MULTILINE,
    )

    new_table = "\n".join(rows)
    if pattern.search(content):
        return pattern.sub(rf"\1{new_table}", content)
    else:
        # If table not found, we might want to warn or just return content
        # For now silent return as it might be custom edited
        return content


def sync_documentation(root: Path, check: bool = False) -> bool:
    """Sync AGENTS.md with current project state.

    Args:
        root: Project root path
        check: If True, only check if sync is needed (for CI)

    Returns:
        True if successful (or if check passed), False otherwise
    """
    agents_file = root / AGENTS_FILE

    if not agents_file.exists():
        print_error(f"{AGENTS_FILE} not found.")
        return False

    print_step("Syncing documentation...")

    try:
        content = agents_file.read_text()
        original_content = content

        content = update_table(content, "🧠 Core Skills", get_skills(root))
        content = update_table(content, "🛡️ Active Rules", get_rules(root))
        content = update_table(content, "🔄 Standard Workflows", get_workflows(root))
        content = update_table(content, "🛠️ Standard Tools", get_tools(root))

        if check:
            if content != original_content:
                print_error("Documentation is out of sync.")
                return False
            else:
                print_success("Documentation is in sync.")
                return True

        if content != original_content:
            agents_file.write_text(content)
            print_success(f"{AGENTS_FILE} updated successfully.")
        else:
            console.print("[info]No changes needed.[/info]")

        return True

    except Exception as e:
        print_error(f"Sync failed: {e}")
        return False
