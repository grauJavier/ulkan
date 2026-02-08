import pyfiglet
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


def print_banner(version: str = None):
    """Prints the Ulkan banner in ASCII art."""
    # "ansi_shadow" or "doom" are good for shadow/filled look.
    # If ansi_shadow isn't available, pyfiglet might fall back or error,
    # but it is a standard FIGlet font.
    try:
        ascii_art = pyfiglet.figlet_format("ULKAN", font="ansi_shadow")
    except pyfiglet.FontNotFound:
        # Fallback to a safe one if ansi_shadow is missing
        ascii_art = pyfiglet.figlet_format("ULKAN", font="doom")

    # Add top spacing
    console.print()

    # Create a "Water/Sky" Gradient
    # We will split the ascii art into lines and apply a vertical gradient
    lines = ascii_art.rstrip().split("\n")

    # Gradient Palette (Top to Bottom): Mist -> Sky -> Deep Spiritual Blue
    gradient_colors = [
        "#eeeeee",  # Mist/White
        "#d0eaff",  # Very Light Blue
        "#87d7ff",  # Sky Blue
        "#5fafff",  # Medium Blue
        "#5f5fff",  # Spiritual Blue
        "#4848d8",  # Deep Blue
    ]

    for i, line in enumerate(lines):
        # Cycle through colors if there are more lines than colors
        color = gradient_colors[min(i, len(gradient_colors) - 1)]
        console.print(f"[bold {color}]{line}[/bold {color}]", justify="center")

    subtitle = "[dim cyan]The Agentic Scaffolding Tool[/dim cyan]"
    if version:
        subtitle += f" [dim cyan]- v{version}[/dim cyan]"

    console.print(subtitle, justify="center", highlight=False)
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
