#!/usr/bin/env python3
"""
Syncs AGENTS.md with current skills, rules, workflows, and tools.
"""

import glob
import os
import re

AGENTS_FILE = "AGENTS.md"
BASE_DIR = ".agent"


def parse_frontmatter(filepath):
    with open(filepath) as f:
        content = f.read()

    name_match = re.search(r"name:\s*(.+)", content)
    trigger_match = re.search(r'trigger:\s*["\'"]?([^"\'"]+)["\'"]?', content)
    desc_match = re.search(r"description:\s*>\s*(.+?)(\n\w|$)", content, re.DOTALL)
    if not desc_match:
        desc_match = re.search(r"description:\s*(.+)", content)

    name = (
        name_match.group(1).strip()
        if name_match
        else os.path.basename(os.path.splitext(filepath)[0])
    )
    trigger = trigger_match.group(1).strip() if trigger_match else "See file"

    desc = "No description."
    if desc_match:
        desc = desc_match.group(1).strip().replace("\n", " ")
        if len(desc) > 100:
            desc = desc[:97] + "..."

    return name, trigger, desc


def get_skills():
    rows = []
    for f in glob.glob(os.path.join(BASE_DIR, "skills/*/SKILL.md")):
        name, trigger, desc = parse_frontmatter(f)
        rows.append(rf"| `{name}` | \"{trigger}\" | {desc} |")
    return sorted(rows)


def get_rules():
    rows = []
    for f in glob.glob(os.path.join(BASE_DIR, "rules/*.md")):
        name, trigger, desc = parse_frontmatter(f)
        if name != "README":
            rows.append(rf"| `{name}` | \"{trigger}\" | {desc} |")
    return sorted(rows)


def get_workflows():
    rows = []
    for f in glob.glob(os.path.join(BASE_DIR, "workflows/*.md")):
        name, trigger, desc = parse_frontmatter(f)
        if name != "README":
            rows.append(rf"| `/{name}` | \"{trigger}\" | {desc} |")
    return sorted(rows)


def get_tools():
    rows = []
    for f in glob.glob(os.path.join(BASE_DIR, "tools/scripts/*")):
        if f.endswith(".py") or f.endswith(".sh"):
            name = os.path.basename(f)
            desc = "Script utility."
            try:
                with open(f) as file:
                    content = file.read(500)
                    doc_match = re.search(r"(\"{3}|\'\'{3})([\s\S]*?)\1", content)
                    if doc_match:
                        desc = doc_match.group(2).strip().replace("\n", " ")[:100]
            except:
                pass
            rows.append(rf"| `{name}` | Script | {desc} |")
    return sorted(rows)


def update_table(content, header, rows):
    if not rows:
        return content
    pattern = re.compile(
        rf"(### {header}[\s\S]*?\| :--- \|\n)([\s\S]*?)(?=\n\n|\n\#)", re.MULTILINE
    )

    new_table = "\n".join(rows)
    if pattern.search(content):
        return pattern.sub(rf"\1{new_table}", content)
    else:
        print(f"Warning: Could not find table for {header}")
        return content


def update_agents_md():
    if not os.path.exists(AGENTS_FILE):
        print(f"Error: {AGENTS_FILE} not found.")
        return

    with open(AGENTS_FILE) as f:
        content = f.read()

    print("Syncing Skills...")
    content = update_table(content, "🧠 Core Skills", get_skills())

    print("Syncing Rules...")
    content = update_table(content, "🛡️ Active Rules", get_rules())

    print("Syncing Workflows...")
    content = update_table(content, "🔄 Standard Workflows", get_workflows())

    print("Syncing Tools...")
    content = update_table(content, "🛠️ Standard Tools", get_tools())

    with open(AGENTS_FILE, "w") as f:
        f.write(content)
    print("✅ AGENTS.md updated successfully.")


if __name__ == "__main__":
    update_agents_md()
