import os
import shutil
from pathlib import Path

from .styles import console, print_error, print_step, print_success


def add_to_gitignore(root: Path, pattern: str) -> None:
    """Adds a pattern to .gitignore if it doesn't already exist."""
    gitignore_file = root / ".gitignore"
    header = "# Ulkan: Agent Adapters Symlinks"

    if not gitignore_file.exists():
        gitignore_file.touch()

    content = gitignore_file.read_text()

    if pattern not in content:
        with gitignore_file.open("a") as f:
            if header not in content:
                f.write(f"\n\n{header}\n")
            f.write(f"{pattern}\n")
        console.print(f"[info]  ➜ Added {pattern} to .gitignore[/info]")


def link_to_agent_folder(root: Path, target_name: str) -> None:
    """Creates a symlink from target_name to .agent folder."""
    agent_dir = root / ".agent"
    target_path = root / target_name

    if not agent_dir.exists():
        print_error(".agent directory not found. Run 'ulkan init' first.")
        return

    # Handle existing target
    if target_path.is_symlink():
        target_path.unlink()
    elif target_path.exists():
        backup = target_path.with_suffix(
            f".backup.{int(os.path.getmtime(target_path))}"
        )
        shutil.move(str(target_path), str(backup))
        console.print(
            f"[warning]  ! Backed up existing {target_name} to {backup.name}[/warning]"
        )

    # Create symlink: .claude -> .agent
    target_path.symlink_to(".agent")
    console.print(f"[info]  ➜ Linked {target_name} -> .agent[/info]")


def link_agents_md_to_root(root: Path, target_name: str) -> None:
    """Creates a symlink from target_name to AGENTS.md at root level."""
    agents_file = root / "AGENTS.md"
    target_path = root / target_name

    if not agents_file.exists():
        console.print("[warning]  ! AGENTS.md not found[/warning]")
        return

    # Handle existing target
    if target_path.is_symlink():
        target_path.unlink()
    elif target_path.exists():
        target_path.unlink()

    # Create symlink: CLAUDE.md -> AGENTS.md
    target_path.symlink_to("AGENTS.md")
    console.print(f"[info]  ➜ Linked {target_name} -> AGENTS.md[/info]")


def link_copilot_instructions(root: Path) -> None:
    """Creates .github/copilot-instructions.md symlink to AGENTS.md."""
    agents_file = root / "AGENTS.md"
    github_dir = root / ".github"
    target_path = github_dir / "copilot-instructions.md"

    if not agents_file.exists():
        console.print("[warning]  ! AGENTS.md not found[/warning]")
        return

    # Create .github if it doesn't exist
    github_dir.mkdir(exist_ok=True)

    # Handle existing target
    if target_path.is_symlink():
        target_path.unlink()
    elif target_path.exists():
        target_path.unlink()

    # Create symlink: .github/copilot-instructions.md -> ../AGENTS.md
    target_path.symlink_to("../AGENTS.md")
    console.print(
        "[info]  ➜ Linked .github/copilot-instructions.md -> AGENTS.md[/info]"
    )


def setup_claude(root: Path) -> None:
    """Configures Claude Code."""
    print_step("Setting up Claude Code...")

    # .claude -> .agent
    link_to_agent_folder(root, ".claude")
    add_to_gitignore(root, ".claude")

    # CLAUDE.md -> AGENTS.md (at root level)
    link_agents_md_to_root(root, "CLAUDE.md")
    add_to_gitignore(root, "CLAUDE.md")

    print_success("Claude Code configured!")


def setup_gemini(root: Path) -> None:
    """Configures Gemini CLI."""
    print_step("Setting up Gemini CLI...")

    # .gemini -> .agent
    link_to_agent_folder(root, ".gemini")
    add_to_gitignore(root, ".gemini")

    # GEMINI.md -> AGENTS.md (at root level)
    link_agents_md_to_root(root, "GEMINI.md")
    add_to_gitignore(root, "GEMINI.md")

    print_success("Gemini CLI configured!")


def setup_codex(root: Path) -> None:
    """Configures Codex (OpenAI)."""
    print_step("Setting up Codex (OpenAI)...")

    # .codex -> .agent
    link_to_agent_folder(root, ".codex")
    add_to_gitignore(root, ".codex")

    # Codex uses AGENTS.md natively, no symlink needed
    print_success("Codex configured! (Uses native AGENTS.md)")


def setup_copilot(root: Path) -> None:
    """Configures GitHub Copilot."""
    print_step("Setting up GitHub Copilot...")

    # .github/copilot-instructions.md -> ../AGENTS.md
    link_copilot_instructions(root)
    add_to_gitignore(root, ".github/copilot-instructions.md")

    print_success("GitHub Copilot configured!")


def setup_opencode(root: Path) -> None:
    """Configures OpenCode."""
    print_step("Setting up OpenCode...")

    # .opencode -> .agent
    link_to_agent_folder(root, ".opencode")
    add_to_gitignore(root, ".opencode")

    # OpenCode reads AGENTS.md natively, no symlink needed
    print_success("OpenCode configured! (Uses native AGENTS.md)")


# ============================================================================
# Removal Functions
# ============================================================================


def remove_symlink_if_valid(path: Path, expected_target: str) -> bool:
    """Remove a symlink only if it points to the expected target.

    Args:
        path: Path to the symlink
        expected_target: Expected target (e.g., '.agent', 'AGENTS.md')

    Returns:
        True if removed, False otherwise
    """
    if not path.is_symlink():
        return False

    target = os.readlink(path)
    if expected_target in target:
        path.unlink()
        console.print(f"[info]  ✓ Removed {path.name}[/info]")
        return True
    return False


def remove_claude(root: Path) -> int:
    """Removes Claude symlinks."""
    print_step("Removing Claude Code symlinks...")
    count = 0
    if remove_symlink_if_valid(root / ".claude", ".agent"):
        count += 1
    if remove_symlink_if_valid(root / "CLAUDE.md", "AGENTS.md"):
        count += 1
    return count


def remove_gemini(root: Path) -> int:
    """Removes Gemini symlinks."""
    print_step("Removing Gemini CLI symlinks...")
    count = 0
    if remove_symlink_if_valid(root / ".gemini", ".agent"):
        count += 1
    if remove_symlink_if_valid(root / "GEMINI.md", "AGENTS.md"):
        count += 1
    return count


def remove_codex(root: Path) -> int:
    """Removes Codex symlinks."""
    print_step("Removing Codex symlinks...")
    count = 0
    if remove_symlink_if_valid(root / ".codex", ".agent"):
        count += 1
    return count


def remove_copilot(root: Path) -> int:
    """Removes Copilot symlinks."""
    print_step("Removing GitHub Copilot symlinks...")
    count = 0
    copilot_path = root / ".github" / "copilot-instructions.md"
    if remove_symlink_if_valid(copilot_path, "AGENTS.md"):
        count += 1
    return count


def remove_opencode(root: Path) -> int:
    """Removes OpenCode symlinks."""
    print_step("Removing OpenCode symlinks...")
    count = 0
    if remove_symlink_if_valid(root / ".opencode", ".agent"):
        count += 1
    return count


# Agent name to remove function mapping
AGENT_REMOVE_MAP = {
    "claude": remove_claude,
    "gemini": remove_gemini,
    "codex": remove_codex,
    "copilot": remove_copilot,
    "opencode": remove_opencode,
}

# Mapping of agent names to their specific documentation file
AGENT_FILE_MAP = {
    "claude": "CLAUDE.md",
    "gemini": "GEMINI.md",
    "codex": "AGENTS.md",
    "copilot": ".github/copilot-instructions.md",
    "opencode": "AGENTS.md",
}
