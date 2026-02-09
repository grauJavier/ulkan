# 🤖 Project Agent Guide (AGENTS.md)

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
| `adr-creator` | "Record decision" | Creates updated Architecture Decision Records (ADRs).   Trigger: When user asks to document a dec... |
| `guidelines-creator` | "Define standard" | Creates strict guidelines or best practices documentation.   Trigger: When user asks to document ... |
| `product-docs-creator` | "Vision/Architecture" | Creates key product documentation (Vision, Architecture) using standard templates.   Trigger: Whe... |
| `rules-creator` | "Add a rule" | Creates new AI agent rules to enforce system constraints.   Trigger: When user asks to define a n... |
| `skill-creator` | "Create/Add a skill" | Creates new AI agent skills following the Agent Skills spec.   Trigger: When user asks to create ... |
| `specs-creator` | "New feature spec" | Creates new technical specifications and feature requirement documents.   Trigger: When user asks... |
| `tools-creator` | "Create a tool/script" | Creates new AI agent tools (scripts, MCP servers, or utilities).   Trigger: When user asks to cre... |
| `workflows-creator` | "Create a workflow" | Creates repeatable workflow documentation.   Trigger: When user asks to define a new process, pro... |

### 🛡️ Active Rules
Always-on constraints that must be followed. **Check `.agent/rules/` for details.**

| Rule | Trigger | Description |
| :--- | :--- | :--- |
| *(Run `ulkan sync` to populate)* | ... | ... |

### 🛠️ Standard Tools
Scripts and utilities available for automation. **Check `.agent/tools/` for details.**

| Tool | Type | Description |
| :--- | :--- | :--- |
| `lint_agent_setup.py` | Script | The Doctor 🩺 Validates the integrity of the .agent configuration. |
| `sync_agents_docs.py` | Script | Syncs AGENTS.md with current skills, rules, workflows, and tools. |

### 🔄 Standard Workflows
Use these workflows to orchestrate complex processes. **Trigger with `/workflow-name`**.

| Workflow | Trigger | Goal |
| :--- | :--- | :--- |
| `/add-to-workflow` | "/add-to-workflow {workflow-names} {instruction}" | Intelligently integrates a new instruction or policy into an existing workflow. |
| `/build` | "New app/From scratch" | Guide for new product definition (Discovery -> Vision -> Architecture) |
| `/docs` | "Check docs" | Maintenance workflow to ensure docs consistency |
| `/feat` | "New feature" | Guide for new features (Spec -> Plan -> Code -> Docs) |
| `/fix` | "Fix bug" | Protocol for bug fixes (Reproduction -> Fix -> Docs) |
| `/git-flow` | "Manage branches / Git flow" | Custom Gitflow workflow (Feature -> Dev -> Release -> Main) |
| `/migrate` | "Migrate project" | Migrate existing agent configs to Ulkan structure |
| `/refact` | "Code smell/Technical Debt" | Workflow for code refactoring (Test Baseline -> Refactor -> Verify) |

---

## 3. Project Context

### 🏗️ Architecture
*   **High-Level**: See [`.agent/docs/product/ARCHITECTURE.md`](.agent/docs/product/ARCHITECTURE.md)
*   **Vision**: See [`.agent/docs/product/VISION.md`](.agent/docs/product/VISION.md)
*   **Decisions**: See [`.agent/docs/decisions/`](.agent/docs/decisions/)

### 🛠️ Tech Stack
*(Agent: Please populate this section during your first analysis)*
*   **Language**: Python 3.12+
*   **Framework**: Typer, Rich, InquirerPy
*   **Database**: N/A (Filesystem)
*   **Infra**: GitHub Actions, PyPI

---

## 4. Maintenance

**This is a living document.**
*   **Adding a Capability**: If you create a new Skill using `skill-creator`, add it to the "Core Skills" table above.
    *   **Tip**: Run `python3 .agent/tools/scripts/sync_agents_docs.py` to auto-update the list!
*   **Adding a Workflow**: If you create a new Workflow using `workflows-creator`, add it to the "Standard Workflows" table.
*   **Updating Specs**: Always update specs in `.agent/docs/specs/` when behavior changes.
