---
name: adr-creator
description: >
  Creates updated Architecture Decision Records (ADRs).
  Trigger: When user asks to document a decision, change component, or record architectural choice.
license: Apache-2.0
metadata:
  author: ulkan
  version: "1.0"
  scope: [root]
  auto_invoke: "Creating new ADR"
trigger: "Record decision"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash, Task
---

## When to Create an ADR

Create an ADR when:
- A significant architectural decision is made.
- A new technology or pattern is introduced.
- A decision has non-trivial trade-offs.
- A previous decision is superseded or deprecated.

## ADR Location

ADRs are located in `.agent/docs/decisions/`.
Format: `{number}-{kebab-case-title}.md` (e.g., `001-use-postgres.md`).

## Resources

- **Templates**: See [assets/](assets/) for ADR-TEMPLATE.md (Michael Nygard format).
