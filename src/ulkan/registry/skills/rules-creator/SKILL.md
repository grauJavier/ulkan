---
name: rules-creator
description: >
  Creates new AI agent rules to enforce system constraints.
  Trigger: When user asks to define a new constraint, policy, convention, or "always-on" rule.
license: Apache-2.0
metadata:
  author: ulkan
  version: "1.0"
  scope: [root]
  auto_invoke: "Creating new rules"
trigger: "Add a rule"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash, Task
---

## When to Create a Rule

Create a rule when:
- A pattern must be enforced across the entire project (or specific scopes)
- Security policies need to be explicitly documented for agents
- Code style conventions are strict and not just "best practices"
- There are "always-on" constraints that agents must never violate

**Don't create a rule when:**
- It's a suggestion or guideline (use `docs/guidelines/` instead)
- It's a temporary constraint
- It's specific to a single file (add a comment instead)

---

## Rule Structure

```
.agent/rules/{rule-name}.md
```

Rules are flat markdown files in `.agent/rules/`.

## Resources

- **Templates**: See [assets/](assets/) for RULE-TEMPLATE.md
