---
name: tools-creator
description: >
  Creates new AI agent tools (scripts, MCP servers, or utilities).
  Trigger: When user asks to create a new tool, script, automation, or system integration.
license: Apache-2.0
metadata:
  author: ulkan
  version: "1.0"
  scope: [root]
  auto_invoke: "Creating new tools"
trigger: "Create a tool/script"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash, Task
---

## When to Create a Tool

Create a tool when:
- An operation needs to be repeatable and robust.
- Complex logic is better handled in Python than Bash one-liners.
- You need to integrate with an external API or service (MCP).
- You need to automate a system task (maintenance, setup, deployment).

## Tool Types & Locations

| Type | Directory | Use Case | Language |
|------|-----------|----------|----------|
| **Scripts** | `.agent/tools/scripts/` | System operations, file manipulation, deployment tasks. | Bash, Python (CLI) |
| **MCP** | `.agent/tools/mcp/` | External API integrations, complex stateful services. | Python |
| **Utils** | `.agent/tools/utils/` | Shared logic, heavy data processing, helper functions. | Python |

## Resources

- **Templates**: See [assets/](assets/) for code templates.
