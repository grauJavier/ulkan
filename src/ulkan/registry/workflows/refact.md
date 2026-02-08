---
description: Workflow for code refactoring (Test Baseline -> Refactor -> Verify)
trigger: "Refactor code"
---
# Refactoring Workflow

## Trigger
Use when improving code structure, readability, or performance WITHOUT changing external behavior.

## Steps

1.  **Analyze & Plan**
    *   Identify the specific code smell or structural issue.
    *   Goal: Improve structure WITHOUT changing behavior.

2.  **Capabilities Check**
    *   Do I need a **Tool** to analyze complexity (e.g., complexity metrics)?

3.  **Safety Check (CRITICAL)**
    *   **Do tests exist for this code?**
        *   **YES**: Run them now to establish a passing baseline.
        *   **NO**: **STOP**. Write tests that cover the current behavior first. Do NOT refactor without a safety net.

4.  **Refactor Cycle**
    *   Make small, atomic changes.
    *   Run tests after *every* single change.
    *   If tests fail, revert immediately to the last green state.

5.  **Docs Check**
    *   Did the refactor change any public API or Interface? -> Update `specs/`.
    *   Did we introduce a new pattern? -> Update `.agent/docs/guidelines/`.

6.  **Definition of Done**
    *   **Linting**: Run `uv run ruff check` and `uv run black .` to ensure the refactor didn't break style.
    *   **Tests**: Verify all tests pass (GREEN).
    *   **CHANGELOG**: (Optional) If the refactor is significant, note it in `CHANGELOG.md` under `Changed`.
