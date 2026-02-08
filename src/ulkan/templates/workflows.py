"""
Standard workflow templates.
"""

FEATURE_DEVELOPMENT_WORKFLOW = """---
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

4.  **Implementation**
    *   Write tests (TDD/BDD if applicable).
    *   Implement the code.
    *   Follow `.agent/docs/guidelines/`.

3.  **Docs Check (Crucial)**
    *   Does this change affect `ARCHITECTURE.md`? -> Update it.
    *   Did we make a significant tech decision? -> Use `adr-creator`.
    *   Did we follow all rules? -> Check `.agent/rules/`.

6.  **Definition of Done**
    *   **CHANGELOG**: Add a new entry to `CHANGELOG.md` under `[Unreleased]`.
    *   **Linting**: Run `uv run ruff check` and `uv run black .` to ensure code style.
    *   **Tests**: Verify all tests pass.
"""

BUG_FIX_WORKFLOW = """---
description: Protocol for bug fixes (Reproduction -> Fix -> Docs)
trigger: "Fix bug"
---
# Bug Fix Workflow

## Trigger
Use when resolving a reported bug or issue.

## Steps

1.  **Reproduction**
    *   Create a test case that reproduces the failure.
    *   Analyze logs and behavior.

2.  **Capabilities Check**
    *   **Skill Check**: Is there a debugging skill in `.agent/skills/`?
    *   **Tool Check**: Do I need a specific Tool to debug this? (If yes, use `tools-creator`).

3.  **Fix**
    *   Implement the fix.
    *   Ensure the test passes.

4.  **Verification**
    *   Run full test suite to ensure no regressions.

5.  **Docs Check**
    *   Was the bug due to a missing or unclear guideline? -> Use `guidelines-creator`.
    *   Does the fix change behavior described in a Spec? -> Update the Spec.

6.  **Definition of Done**
    *   **CHANGELOG**: Add a new entry to `CHANGELOG.md` under `[Unreleased]` with the prefix `Fix:`.
    *   **Linting**: Run `uv run ruff check` and `uv run black .`.
    *   **Tests**: Affirm that the regression test passes and no other tests are broken.
"""

DOCUMENTATION_CHECK_WORKFLOW = """---
description: Maintenance workflow to ensure docs consistency
trigger: "Check docs"
---
# Documentation Check Workflow

## Trigger
Run periodically or before a major release to ensure consistency.

## Steps

1.  **Scan for Outdated Info**
    *   Look for "TODO" comments or placeholders in code.
    *   Check if `AGENTS.md` reflects the current project state.

2.  **Capabilities Check**
    *   Are there manual tasks done frequently that should be a Skill? -> Use `skill-creator`.

3.  **Sync & Validate**
    *   **Run The Doctor**: `python3 .agent/tools/scripts/lint_agent_setup.py`. Fix any issues.
    *   **Run Sync**: `python3 .agent/tools/scripts/sync_agents_docs.py` to update `AGENTS.md`.

4.  **Validate Docs**
    *   Ensure all new features have a Spec.
    *   Ensure `decisions/` contains recent architectural choices.
"""

PRODUCT_INCEPTION_WORKFLOW = """---
description: Guide for new product definition (Discovery -> Vision -> Architecture)
trigger: "New app/From scratch"
---
# Product Inception Workflow

## Trigger
Use when:
1.  **New Project**: Starting "from scratch" or a "new app".
2.  **Existing Project**: Adopting Ulkan late in a project or after migration.

## Steps

1.  **Context Assessment**
    *   **Determine State**: Is this a **greenfield** (empty/new) or **brownfield** (existing code) project?

2.  **Path A: New Project (Greenfield)**
    1.  **Discovery (The "Must Answer" Questions)**
        *   Ask: Problem, Users, Value, Scale.
    2.  **Vision Definition**: Use `product-docs-creator` to generate `.agent/docs/product/VISION.md`.
    3.  **Architecture**: Define tech stack & strategy in `.agent/docs/product/ARCHITECTURE.md`.
    4.  **Capabilities Check**:
        *   **Skills**: Do we need specific frameworks? -> Use `skill-creator`.
        *   **Tools**: Do we need CLI tools? -> Use `tools-creator`.
    5.  **Scaffold**: Create initial folder structure and core files.

3.  **Path B: Existing Project (Brownfield)**
    1.  **Audit**: Analyze existing codebase, tech stack, and patterns.
    2.  **Reverse Engineering**:
        *   Create `VISION.md` reflecting the *current* reality.
        *   Create `ARCHITECTURE.md` documenting the *current* design.
    3.  **Gap Analysis**:
        *   **Skills**: Does the agent need to learn project-specific patterns? -> Use `skill-creator`.
        *   **Tools**: Are there scripts/makefiles we should wrap as Tools? -> Use `tools-creator`.
    4.  **Integration**:
        *   Ensure `AGENTS.md` is fully populated.
        *   Run `/docs` workflow to validate.

4.  **Validation (Both Paths)**
    *   Present the Vision and Architecture to the user.
    *   Ask: "Does this match your intent?"
"""


REFACTORING_WORKFLOW = """---
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
"""

MIGRATE_WORKFLOW = """---
description: Migrate existing agent configs to Ulkan structure
trigger: "Migrate project"
---
# Migration Workflow

## Trigger
Use when adopting Ulkan in a project with existing AI agent configurations.

## Steps

1.  **Assessment**
    *   Identify existing agent folders: `.claude/`, `.gemini/`, etc.
    *   Check for agent-specific files: `CLAUDE.md`, `GEMINI.md`, etc.
    *   Backup important configurations.

2.  **Run Migration**
    *   Run `ulkan migrate --dry-run` to preview changes.
    *   Review the proposed actions.
    *   Run `ulkan migrate` to apply.

3.  **Verification**
    *   Check `.agent/` contains migrated content.
    *   Review `AGENTS.md` for merged content sections.
    *   Verify symlinks are working: `.claude -> .agent`, etc.

4.  **Cleanup**
    *   Review and integrate migrated content into proper sections.
    *   Remove backup files when satisfied.
    *   Run `ulkan init` to ensure complete structure.

5.  **Validation**
    *   Test that your AI agent can read the new structure.
    *   Run `/docs` workflow to validate documentation.
"""
