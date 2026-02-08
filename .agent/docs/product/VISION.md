# Product Vision

## Vision Statement
**Ulkan** empowers developers to bootstrap AI-agent-ready projects in seconds, establishing a standardized architecture that any coding assistant can immediately understand and leverage.

## Target Group
- **Solo developers** who work with AI coding assistants (Claude, Gemini, Copilot, Codex)
- **Teams** wanting to standardize how AI agents interact with their codebase
- **Open source maintainers** who want contributors' AI assistants to follow project conventions

## Needs
| Problem | Solution |
|---------|----------|
| Setting up AI agent configs is repetitive | One `ulkan init` creates everything |
| Each agent has different config locations | `ulkan adapt` creates symlinks to single source |
| No standard for agent skills/workflows | Ulkan provides 8 built-in skills + 5 workflows |
| Documentation scattered across files | `AGENTS.md` as single entry point |

## Product
**Ulkan** is a Python CLI tool that:
1. **Scaffolds** a complete `.agent/` structure with skills, workflows, rules, and docs
2. **Adapts** the structure for specific AI agents via symlinks
3. **Provides** maintenance tools to keep documentation in sync

### Key Features
- `ulkan init` - Full project scaffolding
- `ulkan adapt` - Agent-specific symlinks (Claude, Gemini, Codex, Copilot)
- 8 built-in skills (skill-creator, adr-creator, specs-creator, etc.)
- 5 standard workflows (feature-dev, bug-fix, refactoring, etc.)
- Sync/lint scripts for maintenance

## Business Goals
- Become the de-facto standard for AI-agent project scaffolding
- Foster a community of shared skills and workflows
- Reduce friction in AI-assisted development
