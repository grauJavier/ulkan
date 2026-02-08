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
| *(Run sync tool to populate)* | ... | ... |

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
| `/build` | "New app/From scratch" | Guide for new product definition (Discovery -> Vision -> Architecture) |
| `/docs` | "Check docs" | Maintenance workflow to ensure docs consistency |
| `/feat` | "New feature" | Guide for new features (Spec -> Plan -> Code -> Docs) |
| `/fix` | "Fix bug" | Protocol for bug fixes (Reproduction -> Fix -> Docs) |
| `/migrate` | "Migrate project" | Migrate existing agent configs to Ulkan structure |
| `/refactor` | "Refactor code" | Workflow for code refactoring (Test Baseline -> Refactor -> Verify) |

---

## 3. Project Context

### 🌊 About Ulkan

**Ulkan** is "The Agentic Scaffolding Tool" - a CLI that bootstraps projects with a complete AI-agent-ready architecture.

**Purpose**: Eliminate the friction of setting up AI coding assistant configurations. One command creates a standardized `.agent/` structure with skills, workflows, rules, and documentation that any AI agent can immediately leverage.

### 🏗️ Architecture

```
ulkan/
├── src/ulkan/
│   ├── main.py           # CLI entry point
│   ├── commands.py       # Typer CLI commands (init, adapt)
│   ├── generator.py      # Project structure generation
│   ├── templates/        # Modular template package
│   │   ├── __init__.py   # Re-exports all templates
│   │   ├── agents.py     # AGENTS.md template
│   │   ├── readme.py     # README templates
│   │   ├── skills.py     # Skill creator templates
│   │   ├── workflows.py  # Workflow templates
│   │   └── scripts.py    # Script templates
│   ├── agents.py         # Agent adapter symlink logic
│   ├── builder.py        # AI CLI detection and build logic
│   └── styles.py         # Rich console styling + Ulkan palette
├── pyproject.toml        # Hatchling build config
└── AGENTS.md             # This file
```

**Commands**:
- `ulkan init [PATH]` - Scaffolds `.agent/` and `AGENTS.md`, with interactive agent selection
- `ulkan init -y` - Non-interactive mode (skips all prompts)
- `ulkan adapt` - Creates symlinks for specific AI agents (Claude, Gemini, Codex, Copilot)
- `ulkan build` - Uses adapted agent's CLI to analyze project and update docs
- `ulkan remove <agent>` - Removes symlinks for a specific agent
- `ulkan autoremove` - Removes symlinks for agents without CLI installed

### 🛠️ Tech Stack
*   **Language**: Python 3.12+
*   **CLI Framework**: Typer (with rich markup)
*   **Output Styling**: Rich
*   **Interactive Prompts**: InquirerPy (checkbox multi-select)
*   **Build System**: Hatchling (PEP 517)
*   **Package Manager**: uv

### 📦 Key Design Decisions

1. **Single Source of Truth**: `.agent/` and `AGENTS.md` are the canonical sources. Agent-specific folders (`.claude`, `.gemini`) are symlinks. See [ADR-001](.agent/docs/decisions/001-single-source-of-truth-symlinks.md).
2. **Modular Templates**: Templates organized as a package in `templates/` for maintainability.
3. **Safe File Handling**: `init` skips existing files instead of overwriting, showing `⊘ Skipped: path`.
4. **Ulkan Color Palette**: Consistent styling across CLI using Sky Blue (#87d7ff), Spiritual Blue (#5f5fff), Spring Green (#00ffaf).

---

## 4. Development Commands

```bash
# Install in dev mode
uv sync

# Run CLI
uv run ulkan --help
uv run ulkan init
uv run ulkan adapt --all

# Formatting
uv run black .
uv run ruff check --fix .
```

---

## 5. Maintenance

**This is a living document.**
*   **Adding a Capability**: If you create a new Skill using `skill-creator`, add it to the "Core Skills" table above.
    *   **Tip**: Run `python3 .agent/tools/scripts/sync_agents_docs.py` to auto-update the list!
*   **Adding a Workflow**: If you create a new Workflow using `workflows-creator`, add it to the "Standard Workflows" table.
*   **Updating Specs**: Always update specs in `.agent/docs/specs/` when behavior changes.
