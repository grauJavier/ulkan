# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]



### Added
- `--gitignore` flag to `ulkan init` to automatically add `.agent/` and `AGENTS.md` to `.gitignore`.
- `ulkan list <type>` command to view registry assets.
- `ulkan add <type> <name>` command to add individual assets to the project.
- File-based Registry system replacing hardcoded templates.

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

[Unreleased]: https://github.com/graujavier/ulkan/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/graujavier/ulkan/releases/tag/v0.1.0
