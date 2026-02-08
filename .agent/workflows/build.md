---
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
