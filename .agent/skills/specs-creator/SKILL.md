---
name: specs-creator
description: >
  Creates new technical specifications and feature requirement documents.
  Trigger: When user asks to create a new spec, feature doc, or technical requirement.
license: Apache-2.0
metadata:
  author: ulkan
  version: "1.0"
  scope: [root]
  auto_invoke: "Creating new specs"
trigger: "New feature spec"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash, Task
---

## When to Create a Spec

Create a spec when:
- Starting a new feature or component.
- Documenting complex technical requirements.
- Planning a major refactor or migration.
- The user requests a "spec" or "design doc".

## Spec Location

Specs are located in `.agent/docs/specs/{feature-name}/`.
Each spec should be a self-contained markdown file, e.g., `SPEC.md` or `{feature}-v1.md`.

## Resources

- **Templates**: See [assets/](assets/) for SPEC-TEMPLATE.md.
