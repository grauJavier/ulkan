# 🛠️ Standard Scripts

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
