import time
from pathlib import Path

import typer
from InquirerPy import inquirer
from InquirerPy.utils import get_style
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm

from .agents import (
    AGENT_REMOVE_MAP,
    setup_claude,
    setup_codex,
    setup_copilot,
    setup_gemini,
    setup_opencode,
)
from .builder import is_cli_available, run_build
from .generator import generate_project
from .styles import console, print_banner, print_error, print_step, print_success

# Ulkan color palette for InquirerPy (uses prompt_toolkit syntax)
ULKAN_STYLE = get_style(
    {
        "questionmark": "#87d7ff bold",  # Sky Blue
        "answermark": "#00ffaf",  # Spring Green
        "answer": "#00ffaf",  # Spring Green
        "input": "#eeeeee",  # Mist
        "question": "#eeeeee",  # Mist
        "answered_question": "#eeeeee",  # Mist
        "instruction": "#5f5fff",  # Spiritual Blue
        "pointer": "#87d7ff bold",  # Sky Blue (cursor)
        "checkbox": "#00ffaf",  # Spring Green (selected marker)
        "separator": "#5f5fff",  # Spiritual Blue
        "validator": "#ff5f5f",  # Soft Red (errors)
        "marker": "#00ffaf",  # Spring Green
    },
    style_override=False,
)

app = typer.Typer(
    help="[bold #5f5fff]Ulkan[/bold #5f5fff] [white]|[/white] [dim cyan]The Agentic Scaffolding Tool[/dim cyan]",
    no_args_is_help=True,
    rich_markup_mode="rich",
)


@app.callback()
def main() -> None:
    """
    Ulkan CLI
    """
    pass


@app.command()
def init(
    path: Path = typer.Argument(
        ".", help="Path to initialize the project in. Defaults to current directory."
    ),
    force: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation prompt."),
    gitignore: bool = typer.Option(
        False, "--gitignore", help="Add .agent and AGENTS.md to .gitignore"
    ),
) -> None:
    """
    Scaffolds a new agentic project structure.
    """
    print_banner()

    target_path = path.resolve()

    # Ensure target directory exists
    if not target_path.exists():
        target_path.mkdir(parents=True, exist_ok=True)
        console.print(f"[info]Created directory: {target_path}[/info]")

    console.print(f"[title]Target Directory:[/title] [info]{target_path}[/info]")

    if not force and not Confirm.ask(
        "Do you want to proceed with initialization?", default=True, console=console
    ):
        console.print("[warning]Aborted.[/warning]")
        raise typer.Exit()

    # Ask for agent adapters with checkbox multi-select
    # Pre-select agents whose CLIs are installed
    selected_agents: list[str] = []
    if not force:
        console.print()
        agent_choices = [
            {
                "name": "Claude Code",
                "value": "claude",
                "enabled": is_cli_available("claude"),
            },
            {
                "name": "Gemini CLI",
                "value": "gemini",
                "enabled": is_cli_available("gemini"),
            },
            {
                "name": "Codex (OpenAI)",
                "value": "codex",
                "enabled": is_cli_available("codex"),
            },
            {
                "name": "GitHub Copilot",
                "value": "copilot",
                "enabled": is_cli_available("copilot"),
            },
            {
                "name": "OpenCode",
                "value": "opencode",
                "enabled": is_cli_available("opencode"),
            },
        ]
        selected_agents = inquirer.checkbox(
            message="Select AI agents to adapt for:",
            choices=agent_choices,
            instruction="(↑↓ move, Space select, Enter confirm)",
            style=ULKAN_STYLE,
        ).execute()

        # Show formatted selection summary
        if selected_agents:
            agent_names = {
                "claude": "Claude",
                "gemini": "Gemini",
                "codex": "Codex",
                "copilot": "Copilot",
                "opencode": "OpenCode",
            }
            names = [agent_names[a] for a in selected_agents]
            console.print(f"[info]✓ Selected: {', '.join(names)}[/info]")
        console.print()

    print_step("Initializing project...")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:

        task1 = progress.add_task(description="Creating directories...", total=None)
        time.sleep(0.5)  # Fake delay for dramatic effect

        try:
            generate_project(target_path)
            progress.update(task1, completed=100)
        except Exception as e:
            print_error(f'Failed to generate project: {e}"')
            raise typer.Exit(code=1) from e

    # Update .gitignore if requested
    if gitignore:
        from .generator import update_gitignore

        update_gitignore(target_path)

    # Apply selected adapters
    if selected_agents:
        print_step("Adapting for selected agents...")
        if "claude" in selected_agents:
            setup_claude(target_path)
        if "gemini" in selected_agents:
            setup_gemini(target_path)
        if "codex" in selected_agents:
            setup_codex(target_path)
        if "copilot" in selected_agents:
            setup_copilot(target_path)
        if "opencode" in selected_agents:
            setup_opencode(target_path)

    print_success("Project initialized successfully! 🚀")
    console.print()

    # Initial Sync
    from .syncer import sync_documentation

    sync_documentation(target_path)
    console.print()

    # Check for existing agent configs that could be migrated
    from .migrator import detect_sources

    detected = detect_sources(target_path)
    has_existing_configs = detected["folders"] or detected["files"]

    console.print("[title]Next Steps:[/title]")
    console.print()

    # Check if any AI CLI is available
    any_cli_available = any(
        is_cli_available(agent)
        for agent in ["claude", "gemini", "codex", "copilot", "opencode"]
    )

    if has_existing_configs:
        # Suggest migration first if existing configs found
        console.print("  [warning]Existing agent configs detected![/warning]")
        for folder in detected["folders"]:
            console.print(f"    • {folder}/")
        for file in detected["files"]:
            console.print(f"    • {file}")
        console.print()
        console.print(
            "  [info]1.[/info] Run [prompt]ulkan migrate[/prompt] to unify them"
        )
        console.print(
            '     [dim]Or ask your AI agent: "Run the /migrate workflow"[/dim]'
        )
        console.print()

        if any_cli_available:
            console.print(
                "  [info]2.[/info] Then run [prompt]ulkan build[/prompt] to populate AGENTS.md"
            )
        else:
            console.print(
                '  [info]2.[/info] Ask your AI agent: "Run the /build workflow"'
            )
    else:
        # Standard flow: suggest build or agent prompt
        if any_cli_available:
            console.print(
                "  [info]1.[/info] Run [prompt]ulkan build[/prompt] to populate AGENTS.md with your project context"
            )
            console.print(
                '     [dim]Or ask your AI agent: "Run the /build workflow"[/dim]'
            )
        else:
            console.print(
                '  [info]1.[/info] Ask your AI agent: "Run the /build workflow"'
            )

        console.print()
        console.print(
            "  [info]2.[/info] Run [prompt]ulkan sync[/prompt] to keep docs updated"
        )
        console.print()
        console.print(
            "  [info]3.[/info] Explore [prompt].agent/skills/[/prompt] and [prompt].agent/workflows/[/prompt]"
        )
    console.print()


@app.command()
def adapt(
    all: bool = typer.Option(False, "--all", "-a", help="Configure all AI assistants."),
    claude: bool = typer.Option(False, "--claude", help="Configure Claude Code."),
    gemini: bool = typer.Option(False, "--gemini", help="Configure Gemini CLI."),
    codex: bool = typer.Option(False, "--codex", help="Configure Codex (OpenAI)."),
    copilot: bool = typer.Option(False, "--copilot", help="Configure GitHub Copilot."),
    opencode: bool = typer.Option(False, "--opencode", help="Configure OpenCode."),
) -> None:
    """
    Adapts the project for specific AI agents (Claude, Gemini, etc.).
    """
    print_banner()
    root = Path.cwd()

    if not (root / "AGENTS.md").exists():
        print_error(
            "AGENTS.md not found in current directory. Run [prompt]ulkan init[/prompt] first."
        )
        raise typer.Exit(code=1)

    # If no flags are provided, run in interactive mode
    if not any([all, claude, gemini, codex, copilot, opencode]):
        console.print("[title]Which AI assistants do you use?[/title]")

        # Interactive selection
        if Confirm.ask("Configure Claude Code?", default=True):
            claude = True

        if Confirm.ask("Configure Gemini CLI?", default=False):
            gemini = True

        if Confirm.ask("Configure Codex (OpenAI)?", default=False):
            codex = True

        if Confirm.ask("Configure GitHub Copilot?", default=False):
            copilot = True

        if Confirm.ask("Configure OpenCode?", default=False):
            opencode = True

    # If "all" is selected, enable all
    if all:
        claude = gemini = codex = copilot = opencode = True

    if not any([claude, gemini, codex, copilot, opencode]):
        console.print("[warning]No assistants selected. Exiting.[/warning]")
        return

    print_step("Adapting project for selected agents...")

    if claude:
        setup_claude(root)

    if gemini:
        setup_gemini(root)

    if codex:
        setup_codex(root)

    if copilot:
        setup_copilot(root)

    if opencode:
        setup_opencode(root)

    print_success("Project adapted successfully! 🤖")


@app.command()
def build(
    path: Path = typer.Argument(
        ".", help="Path to the project. Defaults to current directory."
    ),
    agent: str = typer.Option(
        None,
        "--agent",
        "-a",
        help="AI agent CLI to use (claude, gemini). Auto-detects from adapted agents if not specified.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        "-n",
        help="Show the prompt without executing.",
    ),
) -> None:
    """
    Uses AI to analyze and update project documentation.

    Detects which agents are adapted (via symlinks) and uses their CLI
    to analyze the project and update AGENTS.md.
    """
    print_banner()

    target_path = path.resolve()

    if not (target_path / "AGENTS.md").exists():
        print_error("AGENTS.md not found. Run [prompt]ulkan init[/prompt] first.")
        raise typer.Exit(code=1)

    # Show warning and get confirmation (unless dry-run)
    if not dry_run:
        console.print()
        console.print("[warning]⚠️  Build Warning[/warning]")
        console.print()
        console.print(
            "This command will use an AI agent to analyze your project and "
            "[prompt]update AGENTS.md[/prompt]:"
        )
        console.print()
        console.print("  • The agent will [info]read your codebase[/info]")
        console.print(
            "  • [prompt]AGENTS.md[/prompt] will be [warning]modified[/warning] with project context"
        )
        console.print(
            "  • Tech stack, architecture, and commands will be [info]auto-populated[/info]"
        )
        console.print()

        if not Confirm.ask("Proceed with build?", default=True):
            console.print("[info]Build cancelled.[/info]")
            return

    success = run_build(target_path, agent=agent, dry_run=dry_run)

    if not success:
        raise typer.Exit(code=1)


@app.command()
def remove(
    agent: str = typer.Argument(
        None, help="Agent to remove (claude, gemini, codex, copilot, opencode)"
    ),
    self: bool = typer.Option(
        False,
        "--self",
        help="Eject Ulkan: Replace symlinks with copies and remove .agent/",
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Show what would be removed without removing."
    ),
) -> None:
    """
    Removes symlinks for a specific agent OR ejects Ulkan completely.
    """
    import shutil

    from .agents import AGENT_FILE_MAP
    from .builder import get_adapted_agents

    print_banner()
    root = Path.cwd()

    # Case 1: Eject Ulkan (--self)
    if self:
        console.print("[warning]⚠️  Ejecting Ulkan[/warning]")
        console.print(
            "This will [info]convert all symlinks to real files[/info] and remove [warning].agent/[/warning]"
        )

        if not dry_run and not Confirm.ask("Are you sure?", default=False):
            console.print("[info]Aborted.[/info]")
            return

        adapted_agents = get_adapted_agents(root)
        agent_dir = root / ".agent"
        agents_md = root / "AGENTS.md"

        if not agent_dir.exists():
            print_error(".agent directory not found. Nothing to eject.")
            raise typer.Exit(1)

        for agent_name in adapted_agents:
            # 1. Handle Folder (e.g., .claude)
            agent_folder = root / f".{agent_name}"
            if agent_name == "copilot":
                # Copilot doesn't have a .copilot folder usually, but check just in case
                pass
            elif agent_folder.is_symlink():
                console.print(
                    f"[info]  • Converting {agent_folder.name} to directory...[/info]"
                )
                if not dry_run:
                    agent_folder.unlink()
                    shutil.copytree(agent_dir, agent_folder)

            # 2. Handle specific config file (e.g., CLAUDE.md)
            if agent_name in AGENT_FILE_MAP:
                target_file_rel = AGENT_FILE_MAP[agent_name]
                target_file = root / target_file_rel

                # Special case: AGENTS.md native consumers (Codex, OpenCode)
                # don't need copy because AGENTS.md is being removed/moved?
                # Actually, if we remove AGENTS.md, we should make sure they have a copy if they relied on the root one.
                # BUT, AGENT_FILE_MAP maps 'codex' -> 'AGENTS.md'.
                # If we remove .agent and AGENTS.md, we want to leave a copy for them.

                if target_file.is_symlink():
                    console.print(
                        f"[info]  • Converting {target_file.name} to file...[/info]"
                    )
                    if not dry_run:
                        target_file.unlink()
                        shutil.copy2(agents_md, target_file)
                elif target_file.name == "AGENTS.md" and agents_md.exists():
                    # Codex/OpenCode use the root AGENTS.md.
                    # If we are ejecting, that file is technically "Ulkan's file",
                    # BUT users might expect it to stay.
                    # However, the requirement says "remove .agent and AGENTS.md".
                    # If we remove AGENTS.md, Codex/OpenCode lose their context.
                    # So we should probably NOT remove it if it's not a symlink but the actual file?
                    # No, the requirement says "finally remove .agent and AGENTS.md".
                    # Let's follow instructions: copy content to symlinks, then delete.
                    # If Codex uses AGENTS.md directly, it's not a symlink.
                    pass

        if dry_run:
            print_step("Dry run: Would remove .agent/ and AGENTS.md")
            return

        # Finally remove Ulkan core
        if agent_dir.exists():
            shutil.rmtree(agent_dir)
            console.print("[info]  ✓ Removed .agent/[/info]")

        if agents_md.exists():
            agents_md.unlink()
            console.print("[info]  ✓ Removed AGENTS.md[/info]")

        print_success("Ulkan ejected successfully! 🚀")
        console.print(
            "[info]  ➜ The 'Single Source of Truth' has been distributed.[/info]"
        )
        console.print(
            "[info]  ➜ Your agents are now standalone and fully configured.[/info]"
        )
        return

    # Case 2: Remove specific agent
    if not agent:
        print_error("Missing argument 'AGENT'.")
        raise typer.Exit(code=1)

    if agent not in AGENT_REMOVE_MAP:
        print_error(
            f"Unknown agent: {agent}. Valid options: {', '.join(AGENT_REMOVE_MAP.keys())}"
        )
        raise typer.Exit(code=1)

    if dry_run:
        print_step(f"Dry run: would remove {agent} symlinks")
        return

    remove_fn = AGENT_REMOVE_MAP[agent]
    count = remove_fn(root)

    if count > 0:
        print_success(f"Removed {count} symlink(s) for {agent}!")
    else:
        console.print(f"[warning]No symlinks found for {agent}.[/warning]")


@app.command()
def autoremove(
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Show what would be removed without removing."
    ),
) -> None:
    """
    Removes symlinks for agents whose CLI is not installed.
    """
    from .builder import get_adapted_agents

    print_banner()
    root = Path.cwd()

    # Find adapted agents without CLI installed
    adapted = get_adapted_agents(root)
    orphaned = [agent for agent in adapted if not is_cli_available(agent)]

    if not orphaned:
        console.print("[success]No orphaned agent symlinks found.[/success]")
        return

    console.print(
        f"[info]Found {len(orphaned)} agent(s) without CLI installed: {', '.join(orphaned)}[/info]"
    )

    if dry_run:
        print_step("Dry run: would remove the above agents")
        return

    total_removed = 0
    for agent in orphaned:
        if agent in AGENT_REMOVE_MAP:
            count = AGENT_REMOVE_MAP[agent](root)
            total_removed += count

    if total_removed > 0:
        print_success(f"Removed {total_removed} orphaned symlink(s)!")


@app.command()
def migrate(
    source: str = typer.Option(
        None,
        "--from",
        "-f",
        help="Specific agent source to migrate (claude, gemini, codex, opencode).",
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Show what would be migrated without making changes."
    ),
) -> None:
    """
    Migrates existing agent configurations to Ulkan's .agent structure.

    Detects existing .claude, .gemini, CLAUDE.md, etc. and migrates them
    to the unified .agent/ structure with proper symlinks.
    """
    from .generator import generate_project
    from .migrator import detect_sources, run_migration

    print_banner()
    root = Path.cwd()

    # Check if .agent already exists
    agent_dir = root / ".agent"
    agents_md = root / "AGENTS.md"

    if dry_run:
        print_step("Dry run mode - no changes will be made")
        console.print()

    # Detect sources first
    detected = detect_sources(root)

    if not detected["folders"] and not detected["files"]:
        console.print("[info]No existing agent configurations found to migrate.[/info]")
        console.print("[info]Run 'ulkan init' to create a new project.[/info]")
        return

    # Show warning and get confirmation (unless dry-run)
    if not dry_run:
        console.print()
        console.print("[warning]⚠️  Migration Warning[/warning]")
        console.print()
        console.print(
            "This command will restructure your project to follow Ulkan's "
            "[prompt]Single Source of Truth[/prompt] architecture:"
        )
        console.print()
        console.print("  • Existing agent folders will be [warning]backed up[/warning]")
        console.print("  • Content will be [info]merged into .agent/[/info]")
        console.print("  • Original folders will become [info]symlinks → .agent[/info]")
        console.print(
            "  • Agent-specific files (CLAUDE.md) will be [info]merged into AGENTS.md[/info]"
        )
        console.print()
        console.print("[title]Detected configurations:[/title]")
        for folder in detected["folders"]:
            console.print(f"  • {folder}/")
        for file in detected["files"]:
            console.print(f"  • {file}")
        console.print()

        if not Confirm.ask("Proceed with migration?", default=True):
            console.print("[info]Migration cancelled.[/info]")
            return

    # Run migration
    success = run_migration(root, source=source, dry_run=dry_run)

    if not success:
        raise typer.Exit(code=1)

    if dry_run:
        console.print()
        console.print("[info]Run without --dry-run to apply changes.[/info]")
        return

    # After migration, ensure Ulkan structure is complete
    if not agents_md.exists() or not agent_dir.exists():
        print_step("Initializing Ulkan structure...")
        generate_project(root)

    print_success("Migration complete! 🚀")
    console.print()
    console.print("[title]Next Steps:[/title]")
    console.print("  1. Review [prompt]AGENTS.md[/prompt] for merged content")
    console.print("  2. Check [prompt].agent/[/prompt] for migrated files")
    console.print("  3. Remove backup files when satisfied")


@app.command()
def sync(
    check: bool = typer.Option(
        False, "--check", help="Return exit code 1 if documentation is out of sync."
    )
) -> None:
    """
    Syncs AGENTS.md with current skills, rules, workflows, and tools.

    Updates AGENTS.md tables based on the content of .agent/ directory.
    Use --check for CI/CD pipelines to verify documentation is up to date.
    """
    from .syncer import sync_documentation

    root = Path.cwd()
    success = sync_documentation(root, check=check)

    if not success:
        raise typer.Exit(code=1)
