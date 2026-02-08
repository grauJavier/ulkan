"""
Template for the ULKAN_MANUAL.md file.
"""

MANUAL_TEMPLATE_MD = """# 📘 Ulkan Operator's Manual

**Welcome, Agent.**
You are operating within an **Ulkan-scaffolded environment**. This manual is your "Driver's License" for this system. It explains the tools, commands, and structures available to you.

---

## 🚀 1. The Command Line Interface (CLI)

You have access to the `ulkan` CLI. Use it to maintain the project and your own context.

### Core Commands

| Command | Usage | When to use |
| :--- | :--- | :--- |
| **`ulkan sync`** | `ulkan sync` | **ALWAYS** after creating or modifying a Skill, Rule, or Workflow. This updates `AGENTS.md` automatically. |
| **`ulkan build`** | `ulkan build` | When you need to re-analyze the project context and update the "Tech Stack" section of `AGENTS.md`. |
| **`ulkan adapt`** | `ulkan adapt --[agent]` | If you lose your configuration files. Restores symlinks for specific agents (e.g., `ulkan adapt --claude`). |
| **`ulkan migrate`** | `ulkan migrate` | If you find legacy configuration folders (like `.claude/` or `.gemini/`) that need to be unified into `.agent/`. |

---

## 📂 2. The `.agent/` Directory

This is your "brain". All your instructions and capabilities are stored here.

```
.agent/
├── skills/           # YOUR CAPABILITIES. specialized tasks you can perform.
│   ├── skill-creator/
│   ├── adr-creator/
│   └── ...
├── workflows/        # YOUR PROCEDURES. Step-by-step guides for complex tasks.
│   ├── feat.md       # usage: /feat
│   ├── fix.md        # usage: /fix
│   └── ...
├── rules/            # YOUR CONSTRAINTS. "Always-on" policies.
├── docs/             # PROJECT MEMORY.
│   ├── product/      # Vision, Architecture
│   ├── specs/        # Feature Specifications
│   └── decisions/    # Architecture Decision Records (ADRs)
└── tools/            # YOUR HANDS. Scripts and utilities.
    └── scripts/      # Python scripts you can run (e.g., sync_agents_docs.py)
```

---

## 🛠️ 3. How to Use Your Skills

You don't just "write code". You use **Skills** to perform high-value actions.
*   **Need to create a new feature?** -> Check `workflows/feat.md`.
*   **Need to document a decision?** -> Read `skills/adr-creator/SKILL.md` and follow it.
*   **Need to create a new tool?** -> Read `skills/tools-creator/SKILL.md`.

**💡 Pro Tip**: If you are asked to do something complex, **first check if there is a Skill or Workflow for it**. providing a standardized output is better than guessing.

---

## 🔄 4. Self-Correction & Maintenance

### "I created a new Skill but it's not in AGENTS.md!"
> Run `ulkan sync`. This script parses the `.agent/skills` directory and updates the table in `AGENTS.md`.

### "I found a bug in a workflow."
> You are allowed to improve the system! Edit the relevant `.md` file in `.agent/workflows/` and run `ulkan sync`.

### "The project architecture has changed."
> Update `.agent/docs/product/ARCHITECTURE.md`. Keep the documentation alive.

---

*End of Manual.*
"""
