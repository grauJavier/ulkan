---
description: Workflow for code refactoring (Test Baseline -> Refactor -> Verify)
trigger: "Code smell/Technical Debt"
---

# Refactoring Workflow (/refact)

## Trigger
Use when improving code structure, readability, or performance WITHOUT changing external behavior.

## Steps

1.  **Analyze & Plan**
    *   Identify the specific code smell or structural issue.
    *   Goal: Improve structure WITHOUT changing behavior.

2.  **Capabilities Check**
    *   Do I need a **Tool** to analyze complexity (e.g., complexity metrics)?

3.  **Branching**
    *   Follow the branching strategy defined in `/git-flow` (Technical Task).

4.  **Safety Check (CRITICAL)**
    *   **Do tests exist for this code?**
        *   **YES**: Run them now to establish a passing baseline.
        *   **NO**: **STOP**. Write tests that cover the current behavior first. Do NOT refactor without a safety net.

5.  **Refactor Cycle**
    *   Make small, atomic changes.
    *   Run tests after *every* single change.
    *   If tests fail, revert immediately to the last green state.

6.  **Docs Check**
    *   Did the refactor change any public API or Interface? -> Update `specs/`.
    *   Did we introduce a new pattern? -> Update `.agent/docs/guidelines/`.

7.  **Definition of Done**
    *   **Linting**: Run `uv run black .` to ensure code style.
    *   **Tests**: Verify all tests pass (GREEN).
    *   **CHANGELOG**: (Optional) If the refactor is significant, note it in `CHANGELOG.md` under `Changed`.
    *   **Docs**: Run the `/docs` workflow to lint and sync documentation.
    *   **Merge**: Follow the merge strategy defined in `/git-flow`.