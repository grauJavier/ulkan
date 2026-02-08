---
name: workflows-creator
description: >
  Creates repeatable workflow documentation.
  Trigger: When user asks to define a new process, protocol, or standard operating procedure.
license: Apache-2.0
metadata:
  author: ulkan
  version: "1.0"
  scope: [root]
  auto_invoke: "Creating workflow"
trigger: "Create a workflow"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash, Task
---

## When to Create Workflows

Create a workflow when:
- A set of steps needs to be repeated frequently.
- You want to standardize a process (e.g., Feature Dev, Bug Fix).
- Documentation needs to be operationalized.

## Workflows Location

Workflows are located in `.agent/workflows/`.
Format: `{workflow-kebab-case}.md`.

## Resources

- **Templates**: See [assets/](assets/) for WORKFLOW-TEMPLATE.md
