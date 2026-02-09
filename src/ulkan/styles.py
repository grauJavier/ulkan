from rich.console import Console
from rich.theme import Theme

# Palette:
# - Spiritual Blue: #5f5fff
# - Sky Blue: #87d7ff
# - Mist/White: #eeeeee
# - Spring Green: #00ffaf
# - Soft Red: #ff5f5f
# - Soft Orange: #ffaf5f

custom_theme = Theme(
    {
        "info": "dim #eeeeee",  # Mist
        "warning": "bold #00d7af",  # Aqua Green (Verde Agua)
        "error": "bold #ff5f5f",  # Soft Red
        "success": "bold #00ffaf",  # Spring Green
        "prompt": "bold #5f5fff",  # Spiritual Blue
        "title": "bold #87d7ff",  # Sky Blue
        "step": "bold #87d7ff",  # Sky Blue
        "prompt.choices": "bold #00d7af",  # Aqua Green (replaces default magenta)
        "prompt.default": "bold #87d7ff",  # Sky Blue (replaces default cyan)
    }
)

console = Console(theme=custom_theme)


def print_banner(version: str = None, new_version: str = None):
    """Prints the Ulkan banner in ASCII art with wave."""
    # Add top spacing
    console.print()

    # Combined Wave 🌊 + ULKAN ASCII art (wave on left)
    # Wave colors: darker chars are deep blue, lighter are cyan/white
    banner_lines = [
        "   ░▒▒▓▒░    ██╗   ██╗██╗     ██╗  ██╗ █████╗ ███╗   ██╗",
        " ░▓██▓██▓░   ██║   ██║██║     ██║ ██╔╝██╔══██╗████╗  ██║",
        "░███▓▓░ ▒░   ██║   ██║██║     █████╔╝ ███████║██╔██╗ ██║",
        "▒█▓▓▓▒▒      ██║   ██║██║     ██╔═██╗ ██╔══██║██║╚██╗██║",
        "░▒░▒▒▒▒▒░░   ╚██████╔╝███████╗██║  ██╗██║  ██║██║ ╚████║",
        "░▒▒▒░▒▒░▒░   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝",
    ]

    # Gradient Palette (Top to Bottom): Mist -> Sky -> Deep Spiritual Blue
    gradient_colors = [
        "#eeeeee",  # Mist/White
        "#d0eaff",  # Very Light Blue
        "#87d7ff",  # Sky Blue
        "#5fafff",  # Medium Blue
        "#5f5fff",  # Spiritual Blue
        "#4848d8",  # Deep Blue
    ]

    for i, line in enumerate(banner_lines):
        color = gradient_colors[min(i, len(gradient_colors) - 1)]
        console.print(f"[bold {color}]{line}[/bold {color}]", justify="center")

    subtitle = "[dim cyan]The Agentic Scaffolding Tool[/dim cyan]"
    if version:
        subtitle += f" [dim cyan]- v{version}[/dim cyan]"

    console.print(subtitle, justify="center", highlight=False)

    # Show update notification if new version available
    if new_version:
        console.print(
            f"[#ffaf5f]New release available: v{new_version} → Run: ulkan upgrade[/#ffaf5f]",
            justify="center",
        )

    console.print()


def print_step(message: str):
    """Prints a step message with a stylised prefix."""
    console.print(f"[step]➜[/step] {message}")


def print_success(message: str):
    """Prints a success message."""
    console.print(f"[success]✔[/success] {message}")


def print_error(message: str):
    """Prints an error message."""
    console.print(f"[error]✖[/error] {message}")


def print_header(version: str = None, new_version: str = None):
    """Prints a simple one-line header for non-init commands."""
    header = "[bold #5f5fff]Ulkan[/bold #5f5fff] [white]|[/white] [dim cyan]The Agentic Scaffolding Tool[/dim cyan]"
    if version:
        header += f" [dim cyan]- v{version}[/dim cyan]"
    console.print(header)

    # Show update notification if new version available
    if new_version:
        console.print(
            f"[#ffaf5f]New release available: v{new_version} → Run: ulkan upgrade[/#ffaf5f]"
        )

    console.print()
