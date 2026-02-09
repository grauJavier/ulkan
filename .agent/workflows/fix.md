---
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

2.  **Branching**
    *   Follow the branching strategy defined in `/git-flow` (Hotfix or Bugfix).

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
    *   **Linting**: Run `uv run black .`.
    *   **Tests**: Affirm that the regression test passes and no other tests are broken.
    *   **Docs**: Run the `/docs` workflow to lint and sync documentation.
    *   **Merge**: Follow the merge strategy defined in `/git-flow`.
