---
description: Custom Gitflow workflow (Feature -> Dev -> Release -> Main)
trigger: "Manage branches / Git flow"
---
# Gitflow Workflow

## Trigger
Use when managing branching strategy, starting features, releases, or hotfixes.

## Branches Overview
- **`main`**: Production-ready code.
- **`dev`**: Integration branch for features.
- **`feat/*`**: New features (branch off `dev`).
- **`fix/*`**: Bug fixes (branch off `dev` or `main` for hotfixes).
- **`docs/*`**: Documentation changes (branch off `dev`).
- **`style/*`**, **`refactor/*`**, **`perf/*`**, **`test/*`**, **`chore/*`**: Technical tasks (branch off `dev`).
- **`release/*`**: Preparation for new production release (branch off `dev`).

## Commit Convention
Follow Conventional Commits:
- **`feat`**: New feature (e.g., `feat(ui): add dark mode`)
- **`fix`**: Bug fix (e.g., `fix(auth): handle token expiry`)
- **`docs`**: Documentation only (e.g., `docs(readme): update install steps`)
- **`style`**: Formatting, missing semi-colons, etc; no code change (e.g., `style(lint): fix style errors`)
- **`refactor`**: Refactoring production code, eg. renaming a variable (e.g., `refactor(api): simplify user lookup`)
- **`test`**: Adding missing tests, refactoring tests; no production code change (e.g., `test(auth): add login unit tests`)
- **`chore`**: Updating build tasks, package manager configs, etc; no production code change (e.g., `chore(deps): bump ulkan version`)

## Workflows

### 1. Feature Development
Start a new feature:
```bash
git checkout dev
git pull origin dev
git checkout -b feat/my-feature
```
Finish a feature:
1.  Complete work and tests.
2.  Merge into `dev`:
    ```bash
    git checkout dev
    git merge --no-ff feat/my-feature
    git push origin dev
    git branch -d feat/my-feature
    ```

### 2. Release
Start a release:
```bash
git checkout dev
git checkout -b release/1.0.0
# Bump version numbers, update CHANGELOG.md
```
Finish a release:
1.  Merge into `main`:
    ```bash
    git checkout main
    git merge --no-ff release/1.0.0
    git tag -a 1.0.0 -m "Release 1.0.0"
    ```
2.  Merge into `dev`:
    ```bash
    git checkout dev
    git merge --no-ff release/1.0.0
    ```
3.  Delete branch: `git branch -d release/1.0.0`

### 3. Hotfix
Start a hotfix (from main):
```bash
git checkout main
git checkout -b fix/auth-bug
# Fix bug, verify
```
Finish a hotfix:
1.  Merge into `main`:
    ```bash
    git checkout main
    git merge --no-ff fix/auth-bug
    git tag -a 1.0.1 -m "Hotfix 1.0.1"
    ```
2.  Merge into `dev`:
    ```bash
    git checkout dev
    git merge --no-ff fix/auth-bug
    ```
3.  Delete branch: `git branch -d fix/auth-bug`
