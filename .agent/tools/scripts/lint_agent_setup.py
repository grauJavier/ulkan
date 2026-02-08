#!/usr/bin/env python3
"""
The Doctor 🩺
Validates the integrity of the .agent configuration.
"""

import glob
import os
import sys

BASE_DIR = ".agent"
REQUIRED_DIRS = ["skills", "tools", "rules", "workflows", "docs"]


def check_structure():
    errors = []
    for d in REQUIRED_DIRS:
        if not os.path.isdir(os.path.join(BASE_DIR, d)):
            errors.append(f"Missing directory: {d}")
    return errors


def validate_frontmatter(filepath, required_fields):
    try:
        with open(filepath) as f:
            content = f.read()
            parts = content.split("---")
            if len(parts) < 3:
                return f"Invalid YAML frontmatter: {filepath}"

            # Simple field check without yaml library
            for field in required_fields:
                if f"{field}:" not in parts[1]:
                    return f"Missing field '{field}' in {filepath}"
    except Exception as e:
        return f"Error parsing {filepath}: {e}"
    return None


def check_contents():
    errors = []

    # Skills
    for f in glob.glob(os.path.join(BASE_DIR, "skills/*/SKILL.md")):
        err = validate_frontmatter(f, ["name", "description", "trigger"])
        if err:
            errors.append(err)

    # Rules
    for f in glob.glob(os.path.join(BASE_DIR, "rules/*.md")):
        if not f.endswith("README.md"):
            err = validate_frontmatter(f, ["name", "trigger", "scope"])
            if err:
                errors.append(err)

    # Workflows
    for f in glob.glob(os.path.join(BASE_DIR, "workflows/*.md")):
        if not f.endswith("README.md"):
            err = validate_frontmatter(f, ["description", "trigger"])
            if err:
                errors.append(err)

    return errors


def main():
    print("🩺 Running Agent Doctor...")
    structure_errors = check_structure()
    content_errors = check_contents()

    all_errors = structure_errors + content_errors

    if all_errors:
        print("\n❌ Found issues:")
        for e in all_errors:
            print(f" - {e}")
        sys.exit(1)
    else:
        print("\n✅ System looks healthy!")
        sys.exit(0)


if __name__ == "__main__":
    main()
