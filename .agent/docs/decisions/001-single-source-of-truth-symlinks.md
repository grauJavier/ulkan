---
status: accepted
date: 2026-02-08
deciders: graujavier
---

# 001 - Single Source of Truth via Symlinks

## Context and Problem Statement

AI coding assistants (Claude, Gemini, Codex, Copilot) each look for configuration in different locations:
- Claude: `.claude/` folder
- Gemini: `.gemini/` folder
- Copilot: `.github/copilot-instructions.md`
- Codex: `.codex/` folder

How do we maintain consistent configuration across all agents without duplicating files?

## Decision Drivers

* Avoid duplicating configuration that can drift out of sync
* Make it easy to update all agents at once
* Support the "write once, use everywhere" principle
* Keep `.gitignore` clean by ignoring symlinks, not the source

## Considered Options

1. **Duplicate files** - Copy same content to each agent folder
2. **Template generation** - Generate each agent's config from templates
3. **Symlinks to single source** - Use symlinks from agent folders to central location

## Decision Outcome

Chosen option: **Symlinks to single source**, because it:
- Ensures instant propagation of changes (no regeneration needed)
- Provides a clear single source of truth (`.agent/` and `AGENTS.md`)
- Works with Git (symlinks are tracked, content in one place)
- Reduces cognitive load (edit one file, affects all)

### Implementation

```
.claude → .agent       (folder symlink)
.gemini → .agent       (folder symlink)
.codex → .agent        (folder symlink)
CLAUDE.md → AGENTS.md  (file symlink)
GEMINI.md → AGENTS.md  (file symlink)
.github/copilot-instructions.md → ../AGENTS.md
```

### Positive Consequences

* Zero duplication of configuration
* Changes to `.agent/skills/` immediately available to all agents
* Clear mental model: "edit `.agent/`, everything updates"

### Negative Consequences

* Symlinks may confuse some users unfamiliar with the pattern
* Windows support requires administrator privileges or developer mode
* Some tools may not follow symlinks correctly (rare)

## Pros and Cons of the Options

### Option 1: Duplicate files
* Good, because straightforward to implement
* Good, because no symlink complexity
* Bad, because files drift out of sync
* Bad, because double work to update

### Option 2: Template generation
* Good, because allows agent-specific customization
* Bad, because requires regeneration after changes
* Bad, because adds complexity to workflow

### Option 3: Symlinks (chosen)
* Good, because instant propagation
* Good, because single source of truth
* Good, because standard Unix pattern
* Bad, because Windows needs special handling
