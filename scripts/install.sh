#!/bin/bash
# =============================================================================
# 🌊 Ulkan Installer
# The Agentic Scaffolding Tool
# 
# Usage (when repo is public):
#   curl -fsSL https://raw.githubusercontent.com/grauJavier/ulkan/main/scripts/install.sh | bash
#
# Alternative (always works):
#   pip install ulkan
# =============================================================================

set -e

# Colors
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

print_banner() {
    echo -e "${CYAN}"
    echo "  ██╗   ██╗██╗     ██╗  ██╗ █████╗ ███╗   ██╗"
    echo "  ██║   ██║██║     ██║ ██╔╝██╔══██╗████╗  ██║"
    echo "  ██║   ██║██║     █████╔╝ ███████║██╔██╗ ██║"
    echo "  ██║   ██║██║     ██╔═██╗ ██╔══██║██║╚██╗██║"
    echo "  ╚██████╔╝███████╗██║  ██╗██║  ██║██║ ╚████║"
    echo "   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝"
    echo -e "${NC}"
    echo "  The Agentic Scaffolding Tool"
    echo ""
}

info() {
    echo -e "${CYAN}→${NC} $1"
}

success() {
    echo -e "${GREEN}✔${NC} $1"
}

warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

error() {
    echo -e "${RED}✖${NC} $1"
    exit 1
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Detect OS
detect_os() {
    case "$(uname -s)" in
        Linux*)     OS="linux";;
        Darwin*)    OS="macos";;
        CYGWIN*|MINGW*|MSYS*) OS="windows";;
        *)          OS="unknown";;
    esac
    echo "$OS"
}

# Install ulkan using the best available method
install_ulkan() {
    local REPO_URL="git+https://github.com/graujavier/ulkan.git"

    # Try uv first (fastest)
    if command_exists uv; then
        info "Installing ulkan with uv from GitHub..."
        # --force ensures we reinstall/upgrade if it exists
        uv tool install --force "$REPO_URL"
        success "Installed ulkan with uv!"
        return 0
    fi

    # Try pipx (isolated environments)
    if command_exists pipx; then
        info "Installing ulkan with pipx from GitHub..."
        # --force ensures we reinstall/upgrade if it exists
        pipx install --force "$REPO_URL"
        success "Installed ulkan with pipx!"
        return 0
    fi

    # Fallback to pip with --user
    if command_exists pip3; then
        info "Installing ulkan with pip3 from GitHub..."
        pip3 install --upgrade --user "$REPO_URL"
        success "Installed ulkan with pip3!"
        warn "Consider installing pipx for better isolation: https://pipx.pypa.io/"
        check_path_for_pip
        return 0
    fi

    if command_exists pip; then
        info "Installing ulkan with pip from GitHub..."
        pip install --upgrade --user "$REPO_URL"
        success "Installed ulkan with pip!"
        warn "Consider installing pipx for better isolation: https://pipx.pypa.io/"
        check_path_for_pip
        return 0
    fi

    return 1
}

check_path_for_pip() {
    # Simple check if ~/.local/bin matches PATH
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        warn "It seems $HOME/.local/bin is NOT in your PATH."
        warn "You may need to add it to run 'ulkan'."
    fi
}

# Main installation flow
main() {
    print_banner

    OS=$(detect_os)
    info "Detected OS: $OS"

    # Check Python availability
    if ! command_exists python3 && ! command_exists python; then
        error "Python is required but not found. Please install Python 3.12+ first."
    fi

    # Check Python version
    PYTHON_CMD="python3"
    if ! command_exists python3; then
        PYTHON_CMD="python"
    fi

    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
    info "Python version: $PYTHON_VERSION"

    # Install ulkan
    if install_ulkan; then
        echo ""
        success "🌊 Ulkan installed successfully!"
        echo ""
        echo "  Get started:"
        echo "    ulkan init          # Scaffold a new project"
        echo "    ulkan adapt --all   # Set up AI agent configs"
        echo ""
        echo "  Documentation: https://github.com/graujavier/ulkan"
        echo ""
    else
        error "Could not install ulkan. Please install pip, pipx, or uv first."
    fi
}

main "$@"
