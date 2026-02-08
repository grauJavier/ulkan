import shutil
from pathlib import Path
from importlib import resources

from .styles import console

# Define paths to resources
# Assuming they are packaged in src/ulkan/templates and src/ulkan/registry
TEMPLATES_PKG = "ulkan.templates"
REGISTRY_PKG = "ulkan.registry"


def create_directory(path: Path) -> None:
    """Creates a directory if it doesn't exist."""
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)


def copy_resource_file(
    source_path: Path, dest_path: Path, base_path: Path | None = None
) -> bool:
    """Copies a file from source path to destination path.

    Args:
        source_path: Absolute path to source file.
        dest_path: Absolute path to destination file.
        base_path: Optional base path for relative display in logs.

    Returns:
        True if file was created, False if it already existed.
    """
    if dest_path.exists():
        # Show relative path for better context
        display_path = (
            dest_path.relative_to(base_path)
            if base_path
            else f"{dest_path.parent.name}/{dest_path.name}"
        )
        console.print(f"[warning]  ⊘ Skipped: {display_path}[/warning]")
        return False

    # Ensure parent dir exists
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        shutil.copy2(source_path, dest_path)
    except FileNotFoundError:
        console.print(f"[error]  ✖ Error: Source file not found: {source_path}[/error]")
        return False

    # Show success message for created files
    display_path = (
        dest_path.relative_to(base_path)
        if base_path
        else f"{dest_path.parent.name}/{dest_path.name}"
    )
    console.print(f"[title]  ✔ Created: {display_path}[/title]")
    return True


def get_package_path(package_name: str) -> Path:
    """Get the absolute filesystem path of a package."""
    # Simple relative path resolution for now
    current_dir = Path(__file__).parent
    if package_name == "ulkan.templates":
        return current_dir / "templates"
    elif package_name == "ulkan.registry":
        return current_dir / "registry"
    return current_dir


def update_gitignore(base_path: Path) -> None:
    """Updates .gitignore to include .agent and AGENTS.md.

    Args:
        base_path: The root directory of the project.
    """
    gitignore_path = base_path / ".gitignore"
    entries_to_add = [".agent/", "AGENTS.md"]

    if gitignore_path.exists():
        content = gitignore_path.read_text(encoding="utf-8")
        lines = content.splitlines()

        # Check what's missing
        missing = [entry for entry in entries_to_add if entry not in lines]

        if missing:
            with open(gitignore_path, "a", encoding="utf-8") as f:
                if content and not content.endswith("\n"):
                    f.write("\n")
                f.write("\n# Ulkan\n")
                for entry in missing:
                    f.write(f"{entry}\n")
            console.print(
                f"[success]Updated .gitignore with: {', '.join(missing)}[/success]"
            )
        else:
            console.print("[info].gitignore already contains Ulkan entries.[/info]")
    else:
        # Create new .gitignore
        content = "# Ulkan\n" + "\n".join(entries_to_add) + "\n"
        gitignore_path.write_text(content, encoding="utf-8")
        console.print(
            f"[success]Created .gitignore with: {', '.join(entries_to_add)}[/success]"
        )


def generate_project(base_path: Path) -> None:
    """Generates the agentic project structure.

    Args:
        base_path: The root directory where the project will be initialized.
    """

    templates_root = get_package_path(TEMPLATES_PKG)
    registry_root = get_package_path(REGISTRY_PKG)

    if not templates_root.exists():
        console.print(
            f"[error]Templates directory not found at {templates_root}[/error]"
        )
        return

    if not registry_root.exists():
        console.print(f"[error]Registry directory not found at {registry_root}[/error]")
        return

    # 1. Root Manifest (AGENTS.md)
    copy_resource_file(templates_root / "AGENTS.md", base_path / "AGENTS.md", base_path)

    # 2. Core Directories & Scaffolding (READMEs and Manual)
    # We mirror the structure of templates/ into .agent/
    # templates/docs/ULKAN_MANUAL.md -> .agent/docs/ULKAN_MANUAL.md

    agent_dir = base_path / ".agent"

    # Define mapping of template file (relative to templates root) -> destination (relative to .agent root)
    scaffolding_files = {
        "docs/ULKAN_MANUAL.md": "docs/ULKAN_MANUAL.md",
        "skills/README.md": "skills/README.md",
        "tools/README.md": "tools/README.md",
        "tools/scripts/README.md": "tools/scripts/README.md",
        "rules/README.md": "rules/README.md",
        "workflows/README.md": "workflows/README.md",
        "docs/guidelines/README.md": "docs/guidelines/README.md",
        "docs/specs/README.md": "docs/specs/README.md",
        "docs/product/README.md": "docs/product/README.md",
        "docs/decisions/README.md": "docs/decisions/README.md",
    }

    for src_rel, dest_rel in scaffolding_files.items():
        copy_resource_file(templates_root / src_rel, agent_dir / dest_rel, base_path)

    # 3. Registry Components (Skills)
    # Mapping: Skill Name -> Source Folder (relative to registry/skills)
    skills_to_install = [
        "skill-creator",
        "rules-creator",
        "tools-creator",
        "specs-creator",
        "adr-creator",
        "product-docs-creator",
        "guidelines-creator",
        "workflows-creator",
    ]

    for skill in skills_to_install:
        src_skill_dir = registry_root / "skills" / skill
        dest_skill_dir = agent_dir / "skills" / skill

        # Recursively copy the skill folder
        if src_skill_dir.exists():
            # Using copytree functionality manually to use our safe copying/logging
            for src_file in src_skill_dir.rglob("*"):
                if src_file.is_file():
                    rel_path = src_file.relative_to(src_skill_dir)
                    dest_file = dest_skill_dir / rel_path
                    copy_resource_file(src_file, dest_file, base_path)
        else:
            console.print(f"[error]Skill {skill} not found in registry.[/error]")

    # 4. Registry Components (Workflows)
    workflows_to_install = {
        "feat.md": "feat.md",
        "fix.md": "fix.md",
        "docs.md": "docs.md",
        "build.md": "build.md",
        "refact.md": "refact.md",
        "migrate.md": "migrate.md",
    }

    for src_file, dest_file in workflows_to_install.items():
        copy_resource_file(
            registry_root / "workflows" / src_file,
            agent_dir / "workflows" / dest_file,
            base_path,
        )

    # 5. Registry Components (Tools/Scripts)
    scripts_to_install = ["sync_agents_docs.py", "lint_agent_setup.py"]

    for script in scripts_to_install:
        copy_resource_file(
            registry_root / "tools" / "scripts" / script,
            agent_dir / "tools" / "scripts" / script,
            base_path,
        )
