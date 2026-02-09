"""Migrator module for converting existing agent configs to Ulkan structure."""

import os
import shutil
import time
from pathlib import Path

from .styles import console, print_error, print_step, print_success

# Source folder to agent name mapping
SOURCE_FOLDER_MAP = {
    ".claude": "claude",
    ".gemini": "gemini",
    ".codex": "codex",
    ".opencode": "opencode",
}

# Source file to target mapping (agent markdown files)
SOURCE_FILE_MAP = {
    "CLAUDE.md": "claude",
    "GEMINI.md": "gemini",
}


def detect_sources(root: Path) -> dict:
    """Detect existing agent configurations in the project.

    Returns:
        Dict with 'folders' and 'files' lists of detected sources
    """
    detected = {"folders": [], "files": []}

    for folder in SOURCE_FOLDER_MAP:
        path = root / folder
        # Only detect real folders, not symlinks
        if path.exists() and not path.is_symlink():
            detected["folders"].append(folder)

    for file in SOURCE_FILE_MAP:
        path = root / file
        # Only detect real files, not symlinks
        if path.exists() and not path.is_symlink():
            detected["files"].append(file)

    return detected


def create_backup(path: Path) -> Path:
    """Create a timestamped backup of a file or folder.

    Returns:
        Path to the backup
    """
    timestamp = int(time.time())
    backup_name = f"{path.name}.backup.{timestamp}"
    backup_path = path.parent / backup_name

    if path.is_dir():
        shutil.copytree(path, backup_path)
    else:
        shutil.copy2(path, backup_path)

    console.print(f"[info]  ↳ Backup created: {backup_name}[/info]")
    return backup_path


def copy_folder_contents(src: Path, dest: Path) -> int:
    """Copy contents from source folder to destination, merging if needed.

    Returns:
        Number of files copied
    """
    if not dest.exists():
        dest.mkdir(parents=True)

    count = 0
    for item in src.iterdir():
        dest_item = dest / item.name

        if item.is_dir():
            if dest_item.exists():
                # Recursive merge
                count += copy_folder_contents(item, dest_item)
            else:
                shutil.copytree(item, dest_item)
                count += sum(1 for _ in item.rglob("*") if _.is_file())
        else:
            if dest_item.exists():
                # Skip if destination exists (don't overwrite Ulkan blueprints)
                console.print(f"[warning]  ⊘ Skipped (exists): {item.name}[/warning]")
            else:
                shutil.copy2(item, dest_item)
                console.print(f"[info]  ✓ Copied: {item.name}[/info]")
                count += 1

    return count


def merge_agents_md(source_file: Path, agents_md: Path) -> bool:
    """Merge content from a source agent file into AGENTS.md.

    Appends the source content to the "Project Context" section.

    Returns:
        True if merged successfully
    """
    if not source_file.exists():
        return False

    source_content = source_file.read_text()

    if not agents_md.exists():
        # If AGENTS.md doesn't exist, we'll create it during init
        console.print("[warning]  ! AGENTS.md not found, will be created[/warning]")
        return False

    # Add migrated content as a note in the Project Context section
    migration_note = f"""

---
## Migrated Content from {source_file.name}

> The following content was migrated from `{source_file.name}`. Review and integrate as needed.

{source_content}
"""

    # Append to AGENTS.md
    with agents_md.open("a") as f:
        f.write(migration_note)

    console.print(f"[info]  ✓ Merged {source_file.name} into AGENTS.md[/info]")
    return True


def migrate_folder(root: Path, source_name: str, dry_run: bool = False) -> bool:
    """Migrate a source folder to .agent structure.

    Args:
        root: Project root
        source_name: Source folder name (e.g., '.claude')
        dry_run: If True, only show what would happen

    Returns:
        True if migration succeeded
    """
    source_path = root / source_name
    agent_path = root / ".agent"

    if not source_path.exists():
        print_error(f"{source_name} not found")
        return False

    if source_path.is_symlink():
        console.print(f"[info]{source_name} is already a symlink, skipping[/info]")
        return True

    print_step(f"Migrating {source_name} to .agent...")

    if dry_run:
        console.print(f"[info]  Would backup {source_name}[/info]")
        console.print(f"[info]  Would copy contents to .agent/[/info]")
        console.print(f"[info]  Would replace {source_name} with symlink[/info]")
        return True

    # 1. Create backup
    create_backup(source_path)

    # 2. Copy contents to .agent
    if not agent_path.exists():
        agent_path.mkdir(parents=True)

    count = copy_folder_contents(source_path, agent_path)
    console.print(f"[info]  ↳ Copied {count} file(s) to .agent/[/info]")

    # 3. Remove original and create symlink
    shutil.rmtree(source_path)
    source_path.symlink_to(".agent")
    console.print(f"[success]  ✓ {source_name} → .agent[/success]")

    return True


def migrate_file(root: Path, source_name: str, dry_run: bool = False) -> bool:
    """Migrate a source file (e.g., CLAUDE.md) to AGENTS.md.

    Args:
        root: Project root
        source_name: Source file name (e.g., 'CLAUDE.md')
        dry_run: If True, only show what would happen

    Returns:
        True if migration succeeded
    """
    source_path = root / source_name
    agents_path = root / "AGENTS.md"

    if not source_path.exists():
        print_error(f"{source_name} not found")
        return False

    if source_path.is_symlink():
        console.print(f"[info]{source_name} is already a symlink, skipping[/info]")
        return True

    print_step(f"Migrating {source_name} to AGENTS.md...")

    if dry_run:
        console.print(f"[info]  Would backup {source_name}[/info]")
        console.print(f"[info]  Would merge content into AGENTS.md[/info]")
        console.print(f"[info]  Would replace {source_name} with symlink[/info]")
        return True

    # 1. Create backup
    create_backup(source_path)

    # 2. Merge content into AGENTS.md
    if agents_path.exists():
        merge_agents_md(source_path, agents_path)

    # 3. Remove original and create symlink
    source_path.unlink()
    source_path.symlink_to("AGENTS.md")
    console.print(f"[success]  ✓ {source_name} → AGENTS.md[/success]")

    return True


def run_migration(
    root: Path,
    source: str | None = None,
    dry_run: bool = False,
) -> bool:
    """Run the full migration process.

    Args:
        root: Project root path
        source: Specific source to migrate, or None for auto-detect
        dry_run: If True, only show what would happen

    Returns:
        True if migration succeeded
    """
    detected = detect_sources(root)

    if source:
        # Migrate specific source
        if source in SOURCE_FOLDER_MAP.values():
            folder = next(k for k, v in SOURCE_FOLDER_MAP.items() if v == source)
            if folder in detected["folders"]:
                return migrate_folder(root, folder, dry_run)
            else:
                print_error(f"No {folder} folder found to migrate")
                return False
        else:
            print_error(f"Unknown source: {source}")
            return False

    # Auto-detect and migrate all
    if not detected["folders"] and not detected["files"]:
        console.print("[info]No existing agent configurations found to migrate.[/info]")
        console.print("[info]Run 'ulkan init' to create a new project.[/info]")
        return True

    console.print("[title]Detected configurations:[/title]")
    for folder in detected["folders"]:
        console.print(f"  • {folder}/")
    for file in detected["files"]:
        console.print(f"  • {file}")
    console.print()

    success = True

    # Migrate folders first
    for folder in detected["folders"]:
        if not migrate_folder(root, folder, dry_run):
            success = False

    # Then migrate files
    for file in detected["files"]:
        if not migrate_file(root, file, dry_run):
            success = False

    return success
