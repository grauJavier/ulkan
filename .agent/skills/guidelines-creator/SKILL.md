---
name: guidelines-creator
description: >
  Creates strict guidelines or best practices documentation.
  Trigger: When user asks to document coding standards, naming conventions, or recommended workflows.
license: Apache-2.0
metadata:
  author: ulkan
  version: "1.0"
  scope: [root]
  auto_invoke: "Creating guidelines"
trigger: "Define standard"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash, Task
---

## When to Create Guidelines

Create a guideline when:
- Establishing a coding standard (e.g., Python style, React hooks usage).
- Defining a workflow (e.g., Git commit messages, PR process).
- Documenting best practices that are encouraged but not strictly enforced by linter.

## Guidelines Location

Guidelines are located in `.agent/docs/guidelines/`.
Format: `{topic-kebab-case}.md` (e.g., `python-style-guide.md`).

## Resources

- **Templates**: See [assets/](assets/) for GUIDELINE-TEMPLATE.md
