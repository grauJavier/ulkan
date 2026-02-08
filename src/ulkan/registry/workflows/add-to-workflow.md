---
description: Intelligently integrates a new instruction or policy into an existing workflow.
trigger: "/add-to-workflow {workflow-names} {instruction}"
---
# Add to Workflow

## Trigger
Use when you need to incorporate a new policy, tool, or check into one or more workflows (e.g., "Add security scan", "Require approval") and want the AI to intelligently decide where it fits best.
Command: `/add-to-workflow {workflow-names} {instruction}`
Example: `/add-to-workflow git-flow,feat,fix "Add a step to check for sensitive data"`

## Steps

1.  **Analyze the Goal**
    *   Understand the intent of `{instruction}`.
    *   Is it a hard blocker? A suggestion? A verification step?

2.  **Iterate Over Target Workflows**
    *   For each workflow in `{workflow-names}`:
        1.  **Read**: Read `.agent/workflows/{workflow}.md`.
        2.  **Evaluate**: Ask "Is it critical or convenient to add this instruction here?"
        3.  **Optimize**: How can we adjust this specific workflow to perform better?

3.  **Execute Updates**
    *   **Insert**: Add the instruction in the most logical places for each file.
    *   **Refine**: Rewrite existing steps if necessary to merge the new instruction seamlessly.
    *   **Format**: Ensure valid markdown and consistent numbering.

4.  **Documentation Check**
    *   **Sync**: If the workflow title or trigger changed, run `ulkan sync` (or list it as a next step) to update `AGENTS.md`.
    *   **References**: Check if other docs reference this workflow and need updates.

5.  **Final Review**
    *   Does the modified workflow make sense?
    *   Is the new instruction clear and actionable?

6.  **Report to User**
    *   **Confirm Action**: Clearly state: "I have added {instruction} to the following workflows:".
    *   **List Workflows**: List the modified files (e.g., `git-flow.md`).
    *   **Context**: Briefly explain *where* it was added and *why* that spot was chosen (e.g., "Added to 'Commit Convention' section as it relates to message formatting").
