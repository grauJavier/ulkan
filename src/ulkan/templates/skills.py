"""
Skill templates for all 8 skill creators.
"""

# =============================================================================
# SKILL CREATOR
# =============================================================================

SKILL_CREATOR_SKILL_MD = """---
name: skill-creator
description: >
  Creates new AI agent skills following the Agent Skills spec.
  Trigger: When user asks to create a new skill, add agent instructions, or document patterns for AI.
license: Apache-2.0
metadata:
  author: ulkan
  version: "1.0"
  scope: [root]
  auto_invoke: "Creating new skills"
trigger: "Create/Add a skill"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash, WebFetch, WebSearch, Task
---

## When to Create a Skill

Create a skill when:
- A pattern is used repeatedly and AI needs guidance
- Project-specific conventions differ from generic best practices
- Complex workflows need step-by-step instructions
- Decision trees help AI choose the right approach

**Don't create a skill when:**
- Documentation already exists (create a reference instead)
- Pattern is trivial or self-explanatory
- It's a one-off task

---

## Skill Structure

```
skills/{skill-name}/
├── SKILL.md              # Required - main skill file
├── assets/               # Optional - templates, schemas, examples
│   ├── template.py
│   └── schema.json
└── references/           # Optional - links to local docs
    └── docs.md           # Points to docs/developer-guide/*.mdx
```

---

## Naming Conventions

| Type | Pattern | Examples |
|------|---------|----------|
| Generic skill | `{technology}` | `pytest`, `playwright`, `typescript` |
| Project-specific | `project-{component}` | `project-api`, `project-ui` |
| Workflow skill | `{action}-{target}` | `skill-creator`, `jira-task` |

## Resources

- **Templates**: See [assets/](assets/) for SKILL.md template
"""

SKILL_TEMPLATE_MD = """---
name: {skill-name}
description: >
  {Short description of what this skill does}
  Trigger: {When should this skill be used?}
trigger: "{Short trigger phrase for AGENTS.md}"
license: Apache-2.0
metadata:
  author: ulkan
  version: "1.0"
---

## When to Use

Use this skill when:
- {Condition 1}
- {Condition 2}

---

## Critical Patterns

{The MOST important rules - what AI MUST follow}

---

## Code Examples

### Example 1: {Description}

```{language}
{minimal, focused example}
```

---

## Commands

```bash
{command 1}  # {description}
```

---

## Resources

- **Templates**: See [assets/](assets/) for {description of templates}
"""

# =============================================================================
# RULES CREATOR
# =============================================================================

RULES_CREATOR_SKILL_MD = """---
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
"""

RULE_TEMPLATE_MD = """---
name: {rule-name}
description: {Short description of the rule}
trigger: {When this rule applies e.g. "Always", "On Python files"}
scope: {Glob pattern e.g. "**/*.py", "src/legacy/**"}
priority: {High/Medium/Low}
---

## The Rule

{Clear, imperative statement of what rules must be followed or what actions are forbidden.}

## Why

{Brief explanation of the reasoning behind this rule.}

## Valid Examples

### ✅ Do This

```{language}
{code example}
```

## Invalid Examples

### ❌ Don't Do This

```{language}
{code example}
```

## Exceptions

{List any exceptions to this rule, or "None".}

## Enforcement

{How this rule is enforced or verified.}
"""

# =============================================================================
# TOOLS CREATOR
# =============================================================================

TOOLS_CREATOR_SKILL_MD = """---
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
"""

TOOL_TEMPLATE_MD = """---
name: {tool-name}
type: {script | mcp | util}
description: {Short description}
---

## Checklist

- [ ] **Script**: 
    - [ ] `#!/bin/bash` header
    - [ ] `set -e` for safety
    - [ ] Helpful usage/help text (`-h`)
    - [ ] `chmod +x` applied

- [ ] **MCP**:
    - [ ] `import mcp` (or relevant lib)
    - [ ] Defined tools/resources
    - [ ] STDIO communication
    - [ ] Config for checking/restarting

- [ ] **Util**:
    - [ ] Clean function signatures
    - [ ] Type hints
    - [ ] Docstrings

## Snippets

### Bash Script Start

```bash
#!/bin/bash
set -e

# {Description}

function show_help {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help    Show this help message"
}

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    show_help
    exit 0
fi

# Main logic here
```

### Python Utility Start

```python
#!/usr/bin/env python3
\"\"\"
{Description of the utility}
\"\"\"
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="{Description}")
    # Add arguments
    args = parser.parse_args()

    # Logic
    print("Running utility...")

if __name__ == "__main__":
    main()
```
"""

# =============================================================================
# SPECS CREATOR
# =============================================================================

SPECS_CREATOR_SKILL_MD = """---
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
"""

SPEC_TEMPLATE_MD = """---
feature: {feature-name}
status: {draft | in-progress | implemented | deprecated}
last_updated: {YYYY-MM-DD}
title: {Human Readable Title}
owner: {Team or Individual}
priority: {P0 | P1 | P2}
---

## Background

{Context and problem statement. Why are we building this?}

## Requirements

### Functional
- {Requirement 1}
- {Requirement 2}

### Non-Functional
- {Performance, Security, Reliability}

## API Design

{Endpoints, data models, interfaces}

## UI/UX

{Screenshots, wireframes, or descriptions of user interaction}

## Open Questions

- {Question 1}
"""

# =============================================================================
# ADR CREATOR
# =============================================================================

ADR_CREATOR_SKILL_MD = """---
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
"""

ADR_TEMPLATE_MD = """---
status: {proposed | accepted | rejected | deprecated | superseded}
date: {YYYY-MM-DD}
deciders: {list of people involved}
---

# {Title}

## Context and Problem Statement

{Describe the context and problem statement, e.g., in free form using two to three sentences. You may want to articulate the problem in form of a question.}

## Decision Drivers

* {driver 1, e.g., a force, facing concern, …}
* {driver 2, e.g., a force, facing concern, …}

## Considered Options

* {option 1}
* {option 2}
* {option 3}

## Decision Outcome

Chosen option: "{option 1}", because {justification}.

### Positive Consequences

* {positive consequence 1}
* {positive consequence 2}

### Negative Consequences

* {negative consequence 1}
* {negative consequence 2}

## Pros and Cons of the Options

### {option 1}

* Good, because {argument a}
* Good, because {argument b}
* Bad, because {argument c}

### {option 2}

* Good, because {argument a}
* Bad, because {argument b}
"""

# =============================================================================
# PRODUCT DOCS CREATOR
# =============================================================================

PRODUCT_DOCS_CREATOR_SKILL_MD = """---
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
"""

VISION_TEMPLATE_MD = """# Product Vision

## Vision Statement
{Concise, aspiring statement of the future state}

## Target Group
{Who are the users and customers?}

## Needs
{What problem does the product solve? What benefit does it provide?}

## Product
{What product is it? What are the key features?}

## Business Goals
{How will the product benefit the company? Revenue, growth, etc.}
"""

ARCHITECTURE_TEMPLATE_MD = """# System Architecture

## Overview
{High-level description of the system}

## Component Diagram (C4 Context)
```mermaid
graph TD
    User -->|Uses| System
    System -->|Queries| Database
```

## Tech Stack
- **Frontend**: {React, Vue, etc.}
- **Backend**: {Python, Node, etc.}
- **Database**: {Postgres, Mongo, etc.}
- **Infra**: {Docker, K8s, AWS}

## Key Patterns
- {Event Sourcing, CQRS, MVC, etc.}
"""

# =============================================================================
# GUIDELINES CREATOR
# =============================================================================

GUIDELINES_CREATOR_SKILL_MD = """---
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
"""

GUIDELINE_TEMPLATE_MD = """# {Guideline Title}

## Context
{Why is this guideline necessary? What goal does it support?}

## The Guideline
{Clear description of the practice or standard.}

## Examples

### ✅ Do This
```{language}
{Correct example}
```

### ❌ Don't Do This
```{language}
{Incorrect example}
```

## Exceptions
{When does this guideline NOT apply?}
"""

# =============================================================================
# WORKFLOWS CREATOR
# =============================================================================

WORKFLOWS_CREATOR_SKILL_MD = """---
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
"""

WORKFLOW_TEMPLATE_MD = """---
description: {Short description of the workflow}
trigger: {When should this workflow be used?}
---
# {Workflow Title}

## Trigger
{When should this workflow be used? e.g., "Starting a new feature"}

## Steps

1.  **Step 1**
    *   Details...
2.  **Capabilities Check**
    *   Do I need a new Skill (`skill-creator`) or Tool (`tools-creator`)?
3.  **Step 3**
    *   Details...
"""
