# 🌊 Ulkan

[![PyPI version](https://img.shields.io/pypi/v/ulkan.svg)](https://pypi.org/project/ulkan/)
[![Python](https://img.shields.io/pypi/pyversions/ulkan.svg)](https://pypi.org/project/ulkan/)
[![CI](https://github.com/graujavier/ulkan/actions/workflows/ci.yml/badge.svg)](https://github.com/graujavier/ulkan/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/graujavier/ulkan.svg)](LICENSE)

**The Agentic Scaffolding Tool** – Bootstrap AI-agent-ready projects in seconds.

```
  ██╗   ██╗██╗     ██╗  ██╗ █████╗ ███╗   ██╗
  ██║   ██║██║     ██║ ██╔╝██╔══██╗████╗  ██║
  ██║   ██║██║     █████╔╝ ███████║██╔██╗ ██║
  ██║   ██║██║     ██╔═██╗ ██╔══██║██║╚██╗██║
  ╚██████╔╝███████╗██║  ██╗██║  ██║██║ ╚████║
   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
```

## ✨ What is Ulkan?

Ulkan creates a standardized `.agent/` architecture that any AI coding assistant can immediately understand. One command sets up skills, workflows, rules, and documentation for Claude, Gemini, Copilot, and Codex.

## 🚀 Quick Install

**With curl (recommended):**
```bash
curl -fsSL https://raw.githubusercontent.com/graujavier/ulkan/main/scripts/install.sh | bash
```

**With pipx:**
```bash
pipx install ulkan
```

**With uv:**
```bash
uv tool install ulkan
```

**With pip:**
```bash
pip install ulkan
```

## 📦 Usage

### Initialize a Project

```bash
ulkan init
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
| `/product-inception` | New project | Discovery → Vision → Architecture |
| `/feature-development` | New feature | Spec → Plan → Code → Docs |
| `/bug-fix` | Fix bug | Repro → Fix → Verify |
| `/refactoring` | Refactor | Test baseline → Atomic changes |
| `/documentation-check` | Maintenance | Sync and validate docs |

## 🏗️ Why Ulkan?

- **Single Source of Truth**: `.agent/` and `AGENTS.md` are canonical; agent folders are symlinks
- **Zero Configuration**: Works immediately with Claude, Gemini, Copilot, Codex
- **Best Practices Built-in**: Skills, workflows, and ADR templates included
- **Maintenance Tools**: `sync_agents_docs.py` and `lint_agent_setup.py` keep things consistent

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
