---
description: Guide for creating stable GitHub releases (Tag -> Changelog -> Release)
trigger: "Make a release, Release vX.Y.Z, Deploy stable"
---
# Release Workflow

## Trigger
Use when deploying a new stable version of the software.

## Prerequisites
-   Ensure you are on the `dev` branch.
-   Ensure `dev` is up to date with `origin/dev`.
-   Ensure all tests pass.

## Steps

1.  **Preparation**
    *   Create a release branch:
        ```bash
        git checkout dev
        git checkout -b release/vX.Y.Z
        ```

2.  **Version Bump**
    *   Update version in `pyproject.toml` (or `package.json`, etc.).
    *   Update version in `src/ulkan/__init__.py` (if applicable).

3.  **Changelog**
    *   Rename `[Unreleased]` section in `CHANGELOG.md` to `[X.Y.Z] - YYYY-MM-DD`.
    *   Create a new empty `[Unreleased]` section at the top.

4.  **Verification**
    *   Run build check: `uv build` (or relevant build command).
    *   Run tests: `uv run pytest`.

5.  **Commit**
    *   Commit changes:
        ```bash
        git add .
        git commit -m "chore(release): prepare vX.Y.Z"
        ```

6.  **Merge & Tag**
    *   Merge to `main`:
        ```bash
        git checkout main
        git merge --no-ff release/vX.Y.Z
        ```
    *   Create tag:
        ```bash
        git tag -a vX.Y.Z -m "Release vX.Y.Z"
        ```
    *   Back-merge to `dev`:
        ```bash
        git checkout dev
        git merge --no-ff release/vX.Y.Z
        ```

7.  **Push**
    *   Push branches and tags:
        ```bash
        git push origin main dev --tags
        ```

8.  **GitHub Release**
    *   Create release on GitHub (CLI or UI):
        ```bash
        gh release create vX.Y.Z --title "vX.Y.Z" --notes-file CHANGELOG.md
        ```
    *   *Note: If you use the CLI, you might need to extract the specific changelog section.*
