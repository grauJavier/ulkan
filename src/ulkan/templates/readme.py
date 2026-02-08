"""
README templates for all directories.
"""

SKILLS_README_TEMPLATE = """# Skills
Modular capabilities loaded on demand. Each skill should have its own folder with a `SKILL.md`.

👉 **To add a new skill:** Use the `skill-creator` skill.
"""

TOOLS_README_TEMPLATE = """# Tools
MCP configs, scripts, and executable utilities for agents.

👉 **To add a new tool:** Use the `tools-creator` skill.
"""

RULES_README_TEMPLATE = """# Rules
Always-on constraints: code style, security policies, conventions.

👉 **To add a new rule:** Use the `rules-creator` skill.
"""

WORKFLOWS_README_TEMPLATE = """# Workflows
Reusable orchestrated flows triggered with `/`. Chain skills and tools into repeatable processes.

👉 **To add a new workflow:** Use the `workflows-creator` skill.
"""

GUIDELINES_README_TEMPLATE = """# Guidelines
Coding standards, naming conventions, and best practices.

👉 **To add a new guideline:** Use the `guidelines-creator` skill.
"""

SPECS_README_TEMPLATE = """# Specs
Feature specifications and technical requirements.

👉 **To add a new spec:** Use the `specs-creator` skill.
"""

PRODUCT_README_TEMPLATE = """# Product Docs
High-level product documentation like Vision and Architecture.

👉 **To create/reset docs:** Use the `product-docs-creator` skill.
"""

DECISIONS_README_TEMPLATE = """# Decisions (ADRs)
Architecture Decision Records (ADRs) for significant storage decisions.

👉 **To record a decision:** Use the `adr-creator` skill.
"""

SCRIPTS_README_TEMPLATE = """# 🛠️ Standard Scripts

This directory contains executable scripts for maintaining and validating the agent ecosystem.

## 🩺 The Doctor (`lint_agent_setup.py`)

Validates the integrity of the `.agent` folder structure.

*   **Checks**:
    *   Required directories exist.
    *   Frontmatter validity (YAML syntax).
    *   Missing fields (e.g., `trigger`).
*   **Usage**: `python3 .agent/tools/scripts/lint_agent_setup.py`

## 🔄 The Sync (`sync_agents_docs.py`)

Automatically updates the tables in `AGENTS.md`.

*   **Updates**:
    *   🧠 Core Skills
    *   🛡️ Active Rules
    *   🔄 Standard Workflows
    *   🛠️ Standard Tools
*   **Usage**: `python3 .agent/tools/scripts/sync_agents_docs.py`
"""
