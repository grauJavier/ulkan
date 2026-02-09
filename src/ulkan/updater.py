"""Updater module for checking and applying Ulkan updates."""

import subprocess
import sys

import httpx

PYPI_URL = "https://pypi.org/pypi/ulkan/json"


def get_latest_version() -> str | None:
    """Fetches the latest version from PyPI. Returns None if check fails."""
    try:
        response = httpx.get(PYPI_URL, timeout=3.0)
        if response.status_code == 200:
            data = response.json()
            return data.get("info", {}).get("version")
    except (httpx.RequestError, httpx.TimeoutException):
        pass
    return None


def check_for_update(current_version: str) -> tuple[bool, str | None]:
    """
    Checks if a newer version is available.

    Returns:
        (has_update, latest_version) tuple.
        has_update is True if latest > current.
    """
    latest = get_latest_version()
    if latest is None:
        return False, None

    # Simple version comparison (works for semver)
    from packaging.version import Version

    try:
        if Version(latest) > Version(current_version):
            return True, latest
    except Exception:
        # If parsing fails, do string comparison
        if latest != current_version:
            return True, latest

    return False, latest


def run_upgrade() -> bool:
    """
    Upgrades Ulkan to the latest version using pip.

    Returns:
        True if upgrade was successful.
    """
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "ulkan"],
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except Exception:
        return False
