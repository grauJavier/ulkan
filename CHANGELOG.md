# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-02-08

### Added

- Initial release of Ulkan CLI
- `ulkan init` command to scaffold agentic project structure
- `ulkan adapt` command to create symlinks for AI agents
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
- 5 standard workflows:
  - `/product-inception`
  - `/feature-development`
  - `/bug-fix`
  - `/refactoring`
  - `/documentation-check`
- Maintenance scripts:
  - `sync_agents_docs.py`
  - `lint_agent_setup.py`
- Single source of truth architecture via symlinks

[Unreleased]: https://github.com/graujavier/ulkan/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/graujavier/ulkan/releases/tag/v0.1.0
