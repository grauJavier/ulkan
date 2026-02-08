---
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
