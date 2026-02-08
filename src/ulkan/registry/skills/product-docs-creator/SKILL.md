---
name: product-docs-creator
description: >
  Creates key product documentation (Vision, Architecture) using standard templates.
  Trigger: When user asks to create, reset, or initialize product vision or architecture docs.
license: Apache-2.0
metadata:
  author: ulkan
  version: "1.0"
  scope: [root]
  auto_invoke: "Creating product docs"
trigger: "Vision/Architecture"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash, Task
---

## When to Create Product Docs

Use this skill when:
- Starting a new project or module.
- The `VISION.md` or `ARCHITECTURE.md` files are missing.
- You want to reset these documents to a standard structure.

## Document Types & Locations

| Type | File | Description |
|------|------|-------------|
| **Vision** | `.agent/docs/product/VISION.md` | Product goals, target audience, needs. |
| **Architecture** | `.agent/docs/product/ARCHITECTURE.md` | High-level system design, C4 context, stack. |

## Resources

- **Templates**: See [assets/](assets/) for VISION-TEMPLATE.md and ARCHITECTURE-TEMPLATE.md
