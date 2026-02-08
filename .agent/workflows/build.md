---
description: Guide for new product definition (Discovery -> Vision -> Architecture)
trigger: "New app/From scratch"
---
# Product Inception Workflow

## Trigger
Use when the user wants to start a "new app", "new project", or "from scratch".

## Steps

1.  **Discovery (The "Must Answer" Questions)**
    *   Ask the user to define the core essence. Use these questions as a guide:
        1.  **Problem**: What specific pain point are we solving?
        2.  **Users**: Who specifically will use this?
        3.  **Value**: Why will they choose this solution?
        4.  **Scale**: Is this a quick prototype or a production-ready system?

2.  **Capabilities Check**
    *   **Leverage Skills**: Check `.agent/skills/` for architecture, scaffolding, or framework-specific skills.
    *   **Tools**: Do I need to research new **Tools** (e.g., specific framework CLI)?

3.  **Vision Definition**
    *   Use `product-docs-creator` to generate `.agent/docs/product/VISION.md`.
    *   Populate it with the answers from Step 1.

4.  **Architecture & Autonomy**
    *   Define the technical strategy in `.agent/docs/product/ARCHITECTURE.md`.
    *   **Agent Autonomy Guidelines**:
        *   **UI/UX**: Agent has autonomy to use standard, modern best practices.
        *   **Code Structure**: Agent has autonomy to choose folder structure based on framework conventions.
        *   **Libraries**: Agent can suggest/choose standard libraries.
        *   **Major Decisions**: User must approve Database choice, Auth provider, and Hosting strategy.

5.  **Validation**
    *   Present the Vision and Architecture to the user.
    *   Ask: "Does this match your intent?"
