import typer
import time
from pathlib import Path
from rich.prompt import Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn

from .styles import console, print_banner, print_step, print_success, print_error
from .generator import generate_project
from .agents import setup_claude, setup_gemini, setup_codex, setup_copilot

app = typer.Typer(help="Ulkan: The Agentic Foundation Tool", no_args_is_help=True)


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
            print_error(f"Failed to generate project: {e}")
            raise typer.Exit(code=1)

    print_success("Project initialized successfully! 🚀")
    console.print()
    console.print("[title]Next Steps:[/title]")
    console.print("  1. Review [prompt]AGENTS.md[/prompt]")
    console.print("  2. Explore [prompt].agent/skills/[/prompt]")
    console.print(
        "  3. Run [prompt]python3 .agent/tools/scripts/sync_agents_docs.py[/prompt] to update docs."
    )


@app.command()
def adapt(
    all: bool = typer.Option(False, "--all", "-a", help="Configure all AI assistants."),
    claude: bool = typer.Option(False, "--claude", help="Configure Claude Code."),
    gemini: bool = typer.Option(False, "--gemini", help="Configure Gemini CLI."),
    codex: bool = typer.Option(False, "--codex", help="Configure Codex (OpenAI)."),
    copilot: bool = typer.Option(False, "--copilot", help="Configure GitHub Copilot."),
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
    if not any([all, claude, gemini, codex, copilot]):
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

    # If "all" is selected, enable all
    if all:
        claude = gemini = codex = copilot = True

    if not any([claude, gemini, codex, copilot]):
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

    print_success("Project adapted successfully! 🤖")
