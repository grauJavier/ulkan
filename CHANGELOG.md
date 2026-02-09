# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2026-02-09

### Added
- `ulkan uninstall` command to easily remove Ulkan from the system (detects pip, pipx, uv).

## [0.1.1] - 2026-02-09

### Changed
- CI now uses **Black** for formatting instead of Ruff.
- Renamed `release.yml` → `publish.yml` workflow.
- PyPI publishing uses **Trusted Publishers** (OIDC) for secure, tokenless releases.
- Replaced `astral-sh/setup-uv` with `pip install uv` in CI/Release workflows for reliability.

### Added
- `ulkan upgrade` command to update Ulkan to the latest version.
- Update notification in banner/header when a new release is available.
- `--gitignore` flag to `ulkan init` to automatically add `.agent/` and `AGENTS.md` to `.gitignore`.
- `ulkan search <query>` command now queries the Skyll API for agent skills (supports `--sort installs`).
- `ulkan add skill <name>` prioritizes Skyll API and generates YAML frontmatter (`name`, `description`, `trigger`, etc.) instead of `metadata.json`.
- `ulkan list <type>` command to view registry assets (supports `all` to see everything).
- `ulkan add <type> <name>` command to add individual assets to the project.
- File-based Registry system replacing hardcoded templates.
- **New Workflows**:
  - `git-flow`: Standard Gitflow (main/dev) with Conventional Commits.
  - `add-to-workflow`: AI-powered workflow optimizer/injector.
- **CLI Enhancements**: `ulkan add` now provides "Recommended Next Steps" and workflow ProTips.

### Changed
- Renamed `/refactor` workflow to `/refact` for brevity.

## [0.1.0] - 2026-02-08

### Added

- Initial release of Ulkan CLI
- `ulkan init` command to scaffold agentic project structure
- `ulkan adapt` command to create symlinks for AI agents
- `ulkan sync` command to keep AGENTS.md up to date
- `ulkan migrate` command to adopt existing agent configs
- Support for Claude, Gemini, Codex, and Copilot
- 8 built-in skills:
  - `skill-creator`
  - `rules-creator`
  - `tools-creator`
  - `specs-creator`
  - `adr-creator`
  - `product-docs-creator`
  - `guidelines-creator`
  - `workflows-creator`
- 6 standard workflows:
  - `/build`
  - `/feat`
  - `/fix`
  - `/refactor`
  - `/docs`
  - `/migrate`
- Maintenance scripts:
  - `sync_agents_docs.py`
  - `lint_agent_setup.py`
- Single source of truth architecture via symlinks

[Unreleased]: https://github.com/graujavier/ulkan/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/graujavier/ulkan/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/graujavier/ulkan/releases/tag/v0.1.0
