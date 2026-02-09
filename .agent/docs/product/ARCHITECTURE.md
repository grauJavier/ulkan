# Architecture Overview: Ulkan

## 1. High-Level Design

Ulkan operates on a "Hub and Spoke" model:
*   **Hub**: The `.agent/` directory (Single Source of Truth).
*   **Spokes**: The adapter files (e.g., `.claude/`, `copilot-instructions.md`) used by specific tools.
*   **Engine**: The `ulkan` CLI which manages the synchronization between Hub and Spokes.

## 2. Tech Stack

| Component | Technology | Rationale |
| :--- | :--- | :--- |
| **Language** | Python 3.12+ | Modern, typed, compliant with latest standards. |
| **CLI Framework** | `typer` | Type-hint based CLI creation, robust and easy to maintain. |
| **Terminal UI** | `rich` | Beautiful, readable output is critical for developer tools. |
| **Communication** | `httpx` | Modern, async-capable HTTP client for API interactions (PyPI, Skyll). |
| **Versioning** | `packaging` | Robust version comparison logic (SemVer compliant). |

## 3. Project Structure

```
src/ulkan/
├── main.py          # Entry point
├── commands.py      # CLI command definitions (init, build, adapt, sync, upgrade, etc.)
├── agents.py        # Logic for specific AI agent adapters
├── generator.py     # Scaffolding logic (creating .agent structure)
├── migrator.py      # Logic for ingesting existing agent configs
├── syncer.py        # Documentation synchronization logic
├── builder.py       # "AI Build" logic (LLM interaction)
├── manager.py       # Asset management logic (install, list, search)
├── updater.py       # Self-update logic (PyPI check, pip upgrade)
└── blueprints/      # Asset registry (skills, workflows, etc.)
```

## 4. Core Concepts

### 4.1. Single Source of Truth (SSOT)
The `.agent/` folder contains canonical data:
*   `skills/`: Reusable capabilities (e.g., "Create React Component").
*   `workflows/`: Standard operating procedures (e.g., "Bug Fix Workflow").
*   `rules/`: Active constraints.
*   `docs/`: Product context.

### 4.2. Adaptation
The `adapt` command creates symbolic links or generated files mapping the SSOT to vendor-specific formats.
*   *Example*: `.agent` -> `.claude` (Symlink) allows Claude CLI to see the standard structure as its own context.

### 4.3. Synchronization
The `sync` command ensures `AGENTS.md` (the human/agent readable index) reflects the actual state of the `.agent/` directory.

## 5. Data Flow

1.  **User** runs `ulkan init`.
2.  **Generator** creates `.agent/` structure.
3.  **User** runs `ulkan adapt --claude`.
4.  **Adapter** symlinks `.agent` to `.claude`.
5.  **User** runs `ulkan build`.
6.  **Builder** invokes the AI Agent to read project code and populate `AGENTS.md` context sections.
