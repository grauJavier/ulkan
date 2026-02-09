---
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
