"""Builder module for AI CLI integration."""

import shutil
import subprocess
from pathlib import Path

from .styles import console, print_error, print_step, print_success

# Agent to CLI mapping
AGENT_CLI_MAP = {
    "claude": {
        "cli": "claude",
        "check_cmd": ["claude", "--version"],
        "build_cmd": lambda prompt: [
            "claude",
            "-p",
            prompt,
            "--allowedTools",
            "Read,Edit,Bash",
        ],
        "install_hint": "Install with: npm install -g @anthropic-ai/claude-code",
    },
    "gemini": {
        "cli": "gemini",
        "check_cmd": ["gemini", "--version"],
        "build_cmd": lambda prompt: ["gemini", "-p", prompt],
        "install_hint": "Install with: npm install -g @google/gemini-cli",
    },
    "codex": {
        "cli": "codex",
        "check_cmd": ["codex", "--version"],
        "build_cmd": lambda prompt: ["codex", prompt],
        "install_hint": "Install with: npm install -g @openai/codex",
    },
    "copilot": {
        "cli": "gh",
        "check_cmd": ["gh", "copilot", "--version"],
        "build_cmd": lambda prompt: ["gh", "copilot", "suggest", prompt],
        "install_hint": "Install with: gh extension install github/gh-copilot",
    },
    "opencode": {
        "cli": "opencode",
        "check_cmd": ["opencode", "--version"],
        "build_cmd": lambda prompt: ["opencode", prompt],
        "install_hint": "Install with: curl -fsSL https://opencode.ai/install | bash",
    },
}

# Symlink to agent name mapping
SYMLINK_AGENT_MAP = {
    ".claude": "claude",
    ".gemini": "gemini",
    ".codex": "codex",
    ".opencode": "opencode",
}

BUILD_PROMPT = """You are initializing an AI-assisted development environment.

Analyze this project and update AGENTS.md with accurate information:

1. **Project Context**: Update the architecture diagram, tech stack, and commands
2. **Skills/Rules/Workflows**: Check if any project-specific skills should be added
3. **Maintenance**: Run the /docs workflow

Read AGENTS.md first to understand the structure, then make targeted updates.
Do NOT overwrite the entire file - only update sections that need changes.

Current directory: {cwd}
"""


def get_adapted_agents(path: Path) -> list[str]:
    """Returns list of adapted agents based on existing symlinks.

    Args:
        path: Project root path

    Returns:
        List of agent names (e.g., ['claude', 'gemini'])
    """
    adapted = []
    for symlink, agent in SYMLINK_AGENT_MAP.items():
        symlink_path = path / symlink
        if symlink_path.is_symlink():
            adapted.append(agent)
    return adapted


def is_cli_available(agent: str) -> bool:
    """Check if the CLI for an agent is installed.

    Args:
        agent: Agent name ('claude', 'gemini', 'codex', 'copilot')

    Returns:
        True if CLI is available
    """
    import subprocess

    if agent not in AGENT_CLI_MAP:
        return False

    cli_config = AGENT_CLI_MAP[agent]
    cli = cli_config["cli"]

    # First check if base command exists
    if shutil.which(cli) is None:
        return False

    # For agents like copilot that need extension check, run check_cmd
    if agent == "copilot":
        try:
            subprocess.run(
                cli_config["check_cmd"],
                capture_output=True,
                check=True,
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    return True


def get_install_hint(agent: str) -> str:
    """Get installation hint for an agent's CLI."""
    return AGENT_CLI_MAP.get(agent, {}).get("install_hint", "")


def run_build(
    path: Path,
    agent: str | None = None,
    dry_run: bool = False,
) -> bool:
    """Execute build using the specified or detected agent's CLI.

    Args:
        path: Project root path
        agent: Specific agent to use, or None to auto-detect
        dry_run: If True, show prompt without executing

    Returns:
        True if build succeeded
    """
    target_path = path.resolve()

    # Detect adapted agents if not specified
    if agent is None:
        adapted = get_adapted_agents(target_path)
        if not adapted:
            print_error(
                "No agents adapted. Run [bold]ulkan adapt[/bold] first, "
                "or specify an agent with [bold]--agent[/bold]."
            )
            return False

        # Use first adapted agent
        agent = adapted[0]
        if len(adapted) > 1:
            console.print(
                f"[info]Multiple agents adapted: {', '.join(adapted)}. "
                f"Using {agent}.[/info]"
            )

    # Check if CLI is available
    if not is_cli_available(agent):
        print_error(f"{agent} CLI not found.")
        hint = get_install_hint(agent)
        if hint:
            console.print(f"[info]{hint}[/info]")
        return False

    # Build the prompt
    prompt = BUILD_PROMPT.format(cwd=target_path)

    if dry_run:
        print_step("Dry run - would execute:")
        console.print(f"\n[dim]{AGENT_CLI_MAP[agent]['cli']}[/dim] -p")
        console.print(f"\n[info]{prompt}[/info]")
        return True

    # Execute the CLI
    print_step(f"Running {agent} CLI to analyze project...")
    cmd = AGENT_CLI_MAP[agent]["build_cmd"](prompt)

    try:
        subprocess.run(
            cmd,
            cwd=target_path,
            check=True,
            text=True,
        )
        print_success("Build complete!")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Build failed: {e}")
        return False
    except FileNotFoundError:
        print_error(f"{agent} CLI not found in PATH.")
        return False
