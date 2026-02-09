# 🌊 Ulkan | The Agentic Scaffolding Tool

[![PyPI version](https://img.shields.io/pypi/v/ulkan.svg)](https://pypi.org/project/ulkan/)
[![Python](https://img.shields.io/pypi/pyversions/ulkan.svg)](https://pypi.org/project/ulkan/)
[![CI](https://github.com/graujavier/ulkan/actions/workflows/ci.yml/badge.svg)](https://github.com/graujavier/ulkan/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/graujavier/ulkan.svg)](LICENSE)

## ✨ What is Ulkan?

Ulkan creates a standardized `.agent/` architecture that any AI coding assistant can immediately understand. One command sets up skills, workflows, rules, and documentation for Claude, Gemini, Copilot, and Codex.

## 🚀 Quick Install

**With pip (standard):**
```bash
pip install ulkan
```

**With pipx (isolated - recommended):**
```bash
pipx install ulkan
```

**With uv (fastest):**
```bash
uv tool install ulkan
```

## 📦 Usage

### Initialize a Project

```bash
ulkan init
```

Interactive mode prompts for agent selection:
```
? Select AI agents to adapt for: (↑↓ move, Space select, Enter confirm)
  ○ Claude Code
  ○ Gemini CLI
  ○ Codex (OpenAI)
  ○ GitHub Copilot
```

Use `--gitignore` to automatically ignore agent configuration:
```bash
ulkan init --gitignore
```

Or use `-y` for non-interactive mode:
```bash
ulkan init -y --gitignore
```

Creates:
```
your-project/
├── AGENTS.md              # Single entry point for AI agents
└── .agent/
    ├── skills/            # 8 built-in skills
    ├── workflows/         # 5 standard workflows
    ├── rules/             # Project constraints
    ├── tools/             # Scripts and utilities
    └── docs/              # Product documentation
```

### Adapt for AI Agents

```bash
ulkan adapt --all
```

Creates symlinks so all AI assistants share the same configuration:

```
.claude   → .agent       # Claude Code
.gemini   → .agent       # Gemini CLI
.codex    → .agent       # OpenAI Codex
CLAUDE.md → AGENTS.md
GEMINI.md → AGENTS.md
.github/copilot-instructions.md → AGENTS.md
```

### Build Documentation (AI-Powered)

```bash
ulkan build
```

Uses the adapted agent's CLI to analyze your project and update AGENTS.md:
- Detects which agent is adapted (via symlinks)
- Runs the corresponding CLI with a documentation prompt
- Updates project context, architecture, and tech stack

### Update Ulkan

```bash
ulkan upgrade
```

Checks for the latest version on PyPI and upgrades if available. Ulkan also automatically notifies you of new versions in the CLI banner.

### Remove Adapters

```bash
ulkan remove claude    # Removes Claude symlinks
ulkan autoremove       # Removes symlinks for agents without CLI installed
```

## 📦 Registry Commands

Access the built-in registry of skills, workflows, and tools.

### List Assets

```bash
ulkan list all         # List ALL available assets
ulkan list skills      # List available skills
ulkan list workflows   # List available workflows
ulkan list tools       # List available tools/scripts
```

### Add Assets

Add individual components to your project without re-initializing:

```bash
ulkan add skill my-skill           # Adds .agent/skills/my-skill
ulkan add tool scripts/my-script.py # Adds .agent/tools/scripts/my-script.py
```

## 🧠 Built-in Skills

| Skill | Description |
|-------|-------------|
| `skill-creator` | Create new AI agent skills |
| `rules-creator` | Define project constraints |
| `tools-creator` | Build scripts and utilities |
| `specs-creator` | Write feature specifications |
| `adr-creator` | Document architecture decisions |
| `product-docs-creator` | Create Vision & Architecture docs |
| `guidelines-creator` | Define coding standards |
| `workflows-creator` | Create repeatable processes |

## 🔄 Standard Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `/build` | New project | Discovery → Vision → Architecture |
| `/feat` | New feature | Spec → Plan → Code → Docs |
| `/fix` | Fix bug | Repro → Fix → Verify |
| `/refact` | Refactor | Test baseline → Atomic changes |
| `/docs` | Maintenance | Sync and validate docs |
| `/migrate` | Migrate project | Adopt Ulkan in existing projects |
| `/git-flow` | Manage branches | Standard Gitflow with Conventional Commits |
| `/add-to-workflow` | Enhance workflow | Intelligently add steps/rules to workflows |

## 🏗️ Why Ulkan?

- **Single Source of Truth**: `.agent/` and `AGENTS.md` are canonical; agent folders are symlinks
- **Zero Configuration**: Works immediately with Claude, Gemini, Copilot, Codex
- **Best Practices Built-in**: Skills, workflows, and ADR templates included
- **Maintenance Tools**: `ulkan sync` keeps AGENTS.md up to date automatically

## 📚 Documentation

- [AGENTS.md](AGENTS.md) – Project agent guide
- [Architecture](.agent/docs/product/ARCHITECTURE.md) – System design
- [Vision](.agent/docs/product/VISION.md) – Product goals

## 🤝 Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## 📄 License

MIT License – see [LICENSE](LICENSE) for details.

---

**Made with 🌊 for the AI-assisted development community**
