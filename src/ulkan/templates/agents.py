"""
Root manifest template (AGENTS.md).
"""

AGENTS_MD_TEMPLATE = """# 🤖 Project Agent Guide (AGENTS.md)

**Mission**: This file is the definitive guide for any AI Agent working on this project. It defines the Operating Protocol, Available Skills, and Workflows to ensure consistency and high-quality output.

## 1. Operating Protocol

When you start a task, follow this **Search Order**:
1.  **Workflows** (`.agent/workflows/`): Is there a standard procedure for what I'm doing? (e.g., Feature Dev, Bug Fix).
2.  **Rules** (`.agent/rules/`): Are there constraints I must follow?
3.  **Skills** (`.agent/skills/`): Do I have a specific Skill for this? (e.g., creating docs, managing ADRs).

---

## 2. The Agent System

### 🧠 Core Skills
Use these skills to perform specialized tasks. **Check `.agent/skills/` for the full list.**

| Skill | Trigger | Description |
| :--- | :--- | :--- |
| `skill-creator` | "Create/Add a skill" | Scaffolds a new skill directory and guide. |
| `tools-creator` | "Create a tool/script" | Scaffolds scripts, MCP servers, or utilities. |
| `workflows-creator` | "Create a workflow" | Documents a repeatable process. |
| `rules-creator` | "Add a rule" | Defines "always-on" constraints. |
| `specs-creator` | "New feature spec" | Creates technical requirements documents. |
| `product-docs-creator` | "Vision/Architecture" | Manages high-level product documentation. |
| `adr-creator` | "Record decision" | Creates Architecture Decision Records (ADRs). |
| `guidelines-creator` | "Define standard" | Documents coding standards and best practices. |

### 🛡️ Active Rules
Always-on constraints that must be followed. **Check `.agent/rules/` for details.**

| Rule | Trigger | Description |
| :--- | :--- | :--- |
| *(Run `ulkan sync` to populate)* | ... | ... |

### 🛠️ Standard Tools
Scripts and utilities available for automation. **Check `.agent/tools/` for details.**

| Tool | Type | Description |
| :--- | :--- | :--- |
| *(Run `ulkan sync` to populate)* | ... | ... |

### 🔄 Standard Workflows
Use these workflows to orchestrate complex processes. **Trigger with `/workflow-name`**.

| Workflow | Trigger | Goal |
| :--- | :--- | :--- |
| `/build` | "New app", "From scratch" | Discovery -> Vision -> Architecture. |
| `/feat` | "New feature" | Spec -> Plan -> Code -> Verification. |
| `/fix` | "Fix bug" | Repro -> Fix -> Verify -> Docs Update. |
| `/refactor` | "Refactor code" | Safety Check (Tests) -> Atomic Changes. |
| `/docs` | "Check docs", "Maintenance" | Ensure consistency across all docs. |
| `/migrate` | "Migrate project" | Migrate existing agent configs to Ulkan. |

---

## 3. Project Context

### 🏗️ Architecture
*   **High-Level**: See [`.agent/docs/product/ARCHITECTURE.md`](.agent/docs/product/ARCHITECTURE.md)
*   **Vision**: See [`.agent/docs/product/VISION.md`](.agent/docs/product/VISION.md)
*   **Decisions**: See [`.agent/docs/decisions/`](.agent/docs/decisions/)

### 🛠️ Tech Stack
*(Agent: Please populate this section during your first analysis)*
*   **Language**:
*   **Framework**:
*   **Database**:
*   **Infra**:

---

## 4. Maintenance

**This is a living document.**
*   **Adding a Capability**: If you create a new Skill using `skill-creator`, add it to the "Core Skills" table above.
    *   **Tip**: Run `python3 .agent/tools/scripts/sync_agents_docs.py` to auto-update the list!
*   **Adding a Workflow**: If you create a new Workflow using `workflows-creator`, add it to the "Standard Workflows" table.
*   **Updating Specs**: Always update specs in `.agent/docs/specs/` when behavior changes.
"""
