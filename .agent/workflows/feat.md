---
description: Guide for new features (Spec -> Plan -> Code -> Docs)
trigger: "New feature"
---
# Feature Development Workflow

## Trigger
Use when starting a new feature or significant enhancement.

## Steps

1.  **Context & Requirements**
    *   Read `.agent/docs/product/VISION.md` and relevant Specs in `.agent/docs/specs/`.
    *   If no Spec exists, use `specs-creator` to create one.

2.  **Capabilities Check**
    *   **Review Existing Skills**: Check `.agent/skills/` for relevant capabilities.
    *   **Gap Analysis**: Do I need a NEW Skill? (If yes, use `skill-creator`).
    *   **Tools**: Do I need a NEW Tool? (If yes, use `tools-creator`).

3.  **Plan**
    *   Create or update `implementation_plan.md`.
    *   Get user approval.

4.  **Branching**
    *   Follow the branching strategy defined in `/git-flow`.

5.  **Implementation**
    *   Write tests (TDD/BDD if applicable).
    *   Implement the code.
    *   Follow `.agent/docs/guidelines/`.

6.  **Docs Check (Crucial)**
    *   Does this change affect `ARCHITECTURE.md`? -> Update it.
    *   Did we make a significant tech decision? -> Use `adr-creator`.
    *   Did we follow all rules? -> Check `.agent/rules/`.

7.  **Definition of Done**
    *   **CHANGELOG**: Add a new entry to `CHANGELOG.md` under `[Unreleased]`.
    *   **Linting**: Run `uv run black .` to ensure code style.
    *   **Tests**: Verify all tests pass.
    *   **Merge**: Follow the merge strategy defined in `/git-flow`.
