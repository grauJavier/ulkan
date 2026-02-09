# 📘 Ulkan Operator's Manual

Welcome to **Ulkan**, your agentic scaffolding tool. This manual describes how to operate the AI agent system generated for your project.

## 🚀 Quick Start

1.  **Initialize**: You just ran `ulkan init`, so you're set!
2.  **Explore**: Check `.agent/` folder to see your capabilities.
3.  **Sync**: Whenever you add skills or rules manually, run:
    ```bash
    python3 .agent/tools/scripts/sync_agents_docs.py
    ```
    This updates `AGENTS.md` with the latest configuration.

## 🤖 How to Interact

Your AI agent (Rule-based or LLM-driven) should be instructed to read `AGENTS.md` first.

### Triggering Workflows
"Run the feature workflow" -> Agent looks up `/feat` in `AGENTS.md` -> Reads `.agent/workflows/feat.md`.

### Adding Capabilities
Ask the agent:
*   "Create a new skill for React testing" -> Agent uses `skill-creator`.
*   "Create a script to backup DB" -> Agent uses `tools-creator`.
*   "Document a new API standard" -> Agent uses `guidelines-creator`.

## 📂 Directory Structure

*   **`.agent/skills/`**: Atomic capabilities (e.g., `git-commit`, `docker-build`).
*   **`.agent/workflows/`**: Multi-step processes (e.g., `feat.md`, `fix.md`).
*   **`.agent/rules/`**: Inviolable constraints (e.g., `no-console-log.md`).
*   **`.agent/tools/`**: Scripts and utilities.
*   **`.agent/docs/`**: Project documentation (Specs, ADRs, Guidelines).

## 🛠️ Maintenance

*   **Linting**: Run `python3 .agent/tools/scripts/lint_agent_setup.py` to verify structure health.
*   **Version Control**: Commit the entire `.agent` folder to Git. It is the "brain" of your project.

---
*Powered by Ulkan.*
