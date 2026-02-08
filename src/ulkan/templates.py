"""
Templates for the Ulkan CLI generator.
"""

# =============================================================================
# ROOT MANIFEST
# =============================================================================

AGENTS_MD_TEMPLATE = """# 🤖 Project Agent Guide (AGENTS.md)

**Mission**: This file is the definitive guide for any AI Agent working on this project. It defines the Operating Protocol, Available Skills, and Workflows to ensure consistency and high-quality output.

## 1. Operating Protocol

When you start a task, follow this **Search Order**:
1.  **Workflows** (`.agent/workflows/`): Is there a standard procedure for what I'm doing? (e.g., Feature Dev, Bug Fix).
2.  **Rules** (`.agent/rules/`): Are there constraints I must follow?
3.  **Skills** (`.agent/skills/`): Do I have a specific Skill for this? (e.g., creating docs, managing ADRs).

---

## 2. The Agent System

### 🧠 Core Skills
Use these skills to perform specialized tasks. **Check `.agent/skills/` for the full list.**

| Skill | Trigger | Description |
| :--- | :--- | :--- |
| `skill-creator` | "Create/Add a skill" | Scaffolds a new skill directory and guide. |
| `tools-creator` | "Create a tool/script" | Scaffolds scripts, MCP servers, or utilities. |
| `workflows-creator` | "Create a workflow" | Documents a repeatable process. |
| `rules-creator` | "Add a rule" | Defines "always-on" constraints. |
| `specs-creator` | "New feature spec" | Creates technical requirements documents. |
| `product-docs-creator` | "Vision/Architecture" | Manages high-level product documentation. |
| `adr-creator` | "Record decision" | Creates Architecture Decision Records (ADRs). |
| `guidelines-creator` | "Define standard" | Documents coding standards and best practices. |

### 🛡️ Active Rules
Always-on constraints that must be followed. **Check `.agent/rules/` for details.**

| Rule | Trigger | Description |
| :--- | :--- | :--- |
| *(Run sync tool to populate)* | ... | ... |

### 🛠️ Standard Tools
Scripts and utilities available for automation. **Check `.agent/tools/` for details.**

| Tool | Type | Description |
| :--- | :--- | :--- |
| *(Run sync tool to populate)* | ... | ... |

### 🔄 Standard Workflows
Use these workflows to orchestrate complex processes. **Trigger with `/workflow-name`**.

| Workflow | Trigger | Goal |
| :--- | :--- | :--- |
| `/build` | "New app", "From scratch" | Discovery -> Vision -> Architecture. |
| `/feat` | "New feature" | Spec -> Plan -> Code -> Verification. |
| `/fix` | "Fix bug" | Repro -> Fix -> Verify -> Docs Update. |
| `/refact` | "Refactor code" | Safety Check (Tests) -> Atomic Changes. |
| `/docs` | "Check docs", "Maintenance" | Ensure consistency across all docs. |
| `/migrate` | "Migrate project" | Migrate existing agent configs to Ulkan. |

---

## 3. Project Context

### 🏗️ Architecture
*   **High-Level**: See [`.agent/docs/product/ARCHITECTURE.md`](.agent/docs/product/ARCHITECTURE.md)
*   **Vision**: See [`.agent/docs/product/VISION.md`](.agent/docs/product/VISION.md)
*   **Decisions**: See [`.agent/docs/decisions/`](.agent/docs/decisions/)

### 🛠️ Tech Stack
*(Agent: Please populate this section during your first analysis)*
*   **Language**:
*   **Framework**:
*   **Database**:
*   **Infra**:

---

## 4. Maintenance

**This is a living document.**
*   **Adding a Capability**: If you create a new Skill using `skill-creator`, add it to the "Core Skills" table above.
    *   **Tip**: Run `python3 .agent/tools/scripts/sync_agents_docs.py` to auto-update the list!
*   **Adding a Workflow**: If you create a new Workflow using `workflows-creator`, add it to the "Standard Workflows" table.
*   **Updating Specs**: Always update specs in `.agent/docs/specs/` when behavior changes.
"""

# =============================================================================
# README FILES
# =============================================================================

SKILLS_README_TEMPLATE = """# Skills
Modular capabilities loaded on demand. Each skill should have its own folder with a `SKILL.md`.

👉 **To add a new skill:** Use the `skill-creator` skill.
"""

TOOLS_README_TEMPLATE = """# Tools
MCP configs, scripts, and executable utilities for agents.

👉 **To add a new tool:** Use the `tools-creator` skill.
"""

RULES_README_TEMPLATE = """# Rules
Always-on constraints: code style, security policies, conventions.

👉 **To add a new rule:** Use the `rules-creator` skill.
"""

WORKFLOWS_README_TEMPLATE = """# Workflows
Reusable orchestrated flows triggered with `/`. Chain skills and tools into repeatable processes.

👉 **To add a new workflow:** Use the `workflows-creator` skill.
"""

GUIDELINES_README_TEMPLATE = """# Guidelines
Coding standards, naming conventions, and best practices.

👉 **To add a new guideline:** Use the `guidelines-creator` skill.
"""

SPECS_README_TEMPLATE = """# Specs
Feature specifications and technical requirements.

👉 **To add a new spec:** Use the `specs-creator` skill.
"""

PRODUCT_README_TEMPLATE = """# Product Docs
High-level product documentation like Vision and Architecture.

👉 **To create/reset docs:** Use the `product-docs-creator` skill.
"""

DECISIONS_README_TEMPLATE = """# Decisions (ADRs)
Architecture Decision Records (ADRs) for significant storage decisions.

👉 **To record a decision:** Use the `adr-creator` skill.
"""

SCRIPTS_README_TEMPLATE = """# 🛠️ Standard Scripts

This directory contains executable scripts for maintaining and validating the agent ecosystem.

## 🩺 The Doctor (`lint_agent_setup.py`)

Validates the integrity of the `.agent` folder structure.

*   **Checks**:
    *   Required directories exist.
    *   Frontmatter validity (YAML syntax).
    *   Missing fields (e.g., `trigger`).
*   **Usage**: `python3 .agent/tools/scripts/lint_agent_setup.py`

## 🔄 The Sync (`sync_agents_docs.py`)

Automatically updates the tables in `AGENTS.md`.

*   **Updates**:
    *   🧠 Core Skills
    *   🛡️ Active Rules
    *   🔄 Standard Workflows
    *   🛠️ Standard Tools
*   **Usage**: `python3 .agent/tools/scripts/sync_agents_docs.py`
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
\"""
{Description of the utility}
\"""
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

# =============================================================================
# STANDARD WORKFLOWS
# =============================================================================

FEATURE_DEVELOPMENT_WORKFLOW = """---
description: Guide for new features (Spec -> Plan -> Code -> Docs)
trigger: "New feature"
---
# Feature Development Workflow

## Trigger
Use when starting a new feature or significant enhancement.

## Steps

1.  **Context & Requirements**
    *   Read `.agent/docs/product/VISION.md` and relevant Specs in `.agent/docs/specs/`.
    *   If no Spec exists, use `specs-creator` to create one.

2.  **Capabilities Check**
    *   **Review Existing Skills**: Check `.agent/skills/` for relevant capabilities.
    *   **Gap Analysis**: Do I need a NEW Skill? (If yes, use `skill-creator`).
    *   **Tools**: Do I need a NEW Tool? (If yes, use `tools-creator`).

3.  **Plan**
    *   Create or update `implementation_plan.md`.
    *   Get user approval.

4.  **Implementation**
    *   Write tests (TDD/BDD if applicable).
    *   Implement the code.
    *   Follow `.agent/docs/guidelines/`.

5.  **Docs Check (Crucial)**
    *   Does this change affect `ARCHITECTURE.md`? -> Update it.
    *   Did we follow all rules? -> Check `.agent/rules/`.

869: 6.  **Definition of Done**
    *   **CHANGELOG**: Add a new entry to `CHANGELOG.md` under `[Unreleased]`.
    *   **Linting**: Run `uv run ruff check` and `uv run black .` to ensure code style.
    *   **Tests**: Verify all tests pass.
    *   **Docs**: Run the `/docs` workflow to lint and sync documentation.
"""

BUG_FIX_WORKFLOW = """---
description: Protocol for bug fixes (Reproduction -> Fix -> Docs)
trigger: "Fix bug"
---
# Bug Fix Workflow

## Trigger
Use when resolving a reported bug or issue.

## Steps

1.  **Reproduction**
    *   Create a test case that reproduces the failure.
    *   Analyze logs and behavior.

2.  **Capabilities Check**
    *   **Skill Check**: Is there a debugging skill in `.agent/skills/`?
    *   **Tool Check**: Do I need a specific Tool to debug this? (If yes, use `tools-creator`).

3.  **Fix**
    *   Implement the fix.
    *   Ensure the test passes.

4.  **Verification**
    *   Run full test suite to ensure no regressions.

5.  **Docs Check**
    *   Does the fix change behavior described in a Spec? -> Update the Spec.

900: 6.  **Definition of Done**
    *   **CHANGELOG**: Add a new entry to `CHANGELOG.md` under `[Unreleased]` with the prefix `Fix:`.
    *   **Linting**: Run `uv run ruff check` and `uv run black .`.
    *   **Tests**: Affirm that the regression test passes and no other tests are broken.
    *   **Docs**: Run the `/docs` workflow to lint and sync documentation.
"""

DOCUMENTATION_CHECK_WORKFLOW = """---
description: Maintenance workflow to ensure docs consistency
trigger: "Check docs"
---
# Documentation Check Workflow

## Trigger
Run periodically or before a major release to ensure consistency.

## Steps

1.  **Scan for Outdated Info**
    *   Look for "TODO" comments or placeholders in code.
    *   Check if `AGENTS.md` reflects the current project state.

2.  **Capabilities Check**
    *   Are there manual tasks done frequently that should be a Skill? -> Use `skill-creator`.

3.  **Sync & Validate**
    *   **Run The Doctor**: `python3 .agent/tools/scripts/lint_agent_setup.py`. Fix any issues.
    *   **Run Sync**: `python3 .agent/tools/scripts/sync_agents_docs.py` to update `AGENTS.md`.

4.  **Validate Docs**
    *   Ensure all new features have a Spec.
    *   Ensure `decisions/` contains recent architectural choices.
"""

PRODUCT_INCEPTION_WORKFLOW = """---
description: Guide for new product definition (Discovery -> Vision -> Architecture)
trigger: "New app/From scratch"
---
# Product Inception Workflow

## Trigger
Use when the user wants to start a "new app", "new project", or "from scratch".

## Steps

1.  **Discovery (The "Must Answer" Questions)**
    *   Ask the user to define the core essence. Use these questions as a guide:
        1.  **Problem**: What specific pain point are we solving?
        2.  **Users**: Who specifically will use this?
        3.  **Value**: Why will they choose this solution?
        4.  **Scale**: Is this a quick prototype or a production-ready system?

2.  **Capabilities Check**
    *   **Leverage Skills**: Check `.agent/skills/` for architecture, scaffolding, or framework-specific skills.
    *   **Tools**: Do I need to research new **Tools** (e.g., specific framework CLI)?

3.  **Vision Definition**
    *   Use `product-docs-creator` to generate `.agent/docs/product/VISION.md`.
    *   Populate it with the answers from Step 1.

4.  **Architecture & Autonomy**
    *   Define the technical strategy in `.agent/docs/product/ARCHITECTURE.md`.
    *   **Agent Autonomy Guidelines**:
        *   **UI/UX**: Agent has autonomy to use standard, modern best practices.
        *   **Code Structure**: Agent has autonomy to choose folder structure based on framework conventions.
        *   **Libraries**: Agent can suggest/choose standard libraries.
        *   **Major Decisions**: User must approve Database choice, Auth provider, and Hosting strategy.

5.  **Validation**
    *   Present the Vision and Architecture to the user.
    *   Ask: "Does this match your intent?"
    *   **Docs**: Run the `/docs` workflow to lint and sync documentation.
"""

REFACTORING_WORKFLOW = """---
description: Workflow for code refactoring (Test Baseline -> Refactor -> Verify)
trigger: "Refactor code"
---
# Refactoring Workflow (/refact)

## Trigger
Use when improving code structure, readability, or performance WITHOUT changing external behavior.

## Steps

1.  **Analyze & Plan**
    *   Identify the specific code smell or structural issue.
    *   Goal: Improve structure WITHOUT changing behavior.

2.  **Capabilities Check**
    *   Do I need a **Tool** to analyze complexity (e.g., complexity metrics)?

3.  **Safety Check (CRITICAL)**
    *   **Do tests exist for this code?**
        *   **YES**: Run them now to establish a passing baseline.
        *   **NO**: **STOP**. Write tests that cover the current behavior first. Do NOT refactor without a safety net.

4.  **Refactor Cycle**
    *   Make small, atomic changes.
    *   Run tests after *every* single change.
    *   If tests fail, revert immediately to the last green state.

5.  **Docs Check**
    *   Did we introduce a new pattern? -> Update `.agent/docs/guidelines/`.

999: 6.  **Definition of Done**
    *   **Linting**: Run `uv run ruff check` and `uv run black .` to ensure the refactor didn't break style.
    *   **Tests**: Verify all tests pass (GREEN).
    *   **CHANGELOG**: (Optional) If the refactor is significant, note it in `CHANGELOG.md` under `Changed`.
    *   **Docs**: Run the `/docs` workflow to lint and sync documentation.
"""

# =============================================================================
# SCRIPTS
# =============================================================================

SYNC_AGENTS_DOCS_PY = '''#!/usr/bin/env python3
"""
Syncs AGENTS.md with current skills, rules, workflows, and tools.
"""
import os
import re
import glob

AGENTS_FILE = "AGENTS.md"
BASE_DIR = ".agent"

def parse_frontmatter(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    name_match = re.search(r'name:\\s*(.+)', content)
    trigger_match = re.search(r'trigger:\\s*["\\'"]?([^"\\'"]+)["\\'"]?', content)
    desc_match = re.search(r'description:\\s*>\\s*(.+?)(\\n\\w|$)', content, re.DOTALL)
    if not desc_match:
         desc_match = re.search(r'description:\\s*(.+)', content)

    name = name_match.group(1).strip() if name_match else os.path.basename(os.path.splitext(filepath)[0])
    trigger = trigger_match.group(1).strip() if trigger_match else "See file"
    
    desc = "No description."
    if desc_match:
        desc = desc_match.group(1).strip().replace('\\n', ' ')
        if len(desc) > 100: desc = desc[:97] + "..."
    
    return name, trigger, desc

def get_skills():
    rows = []
    for f in glob.glob(os.path.join(BASE_DIR, "skills/*/SKILL.md")):
        name, trigger, desc = parse_frontmatter(f)
        rows.append(rf"| `{name}` | \\"{trigger}\\" | {desc} |")
    return sorted(rows)

def get_rules():
    rows = []
    for f in glob.glob(os.path.join(BASE_DIR, "rules/*.md")):
        name, trigger, desc = parse_frontmatter(f)
        if name != "README":
            rows.append(rf"| `{name}` | \\"{trigger}\\" | {desc} |")
    return sorted(rows)

def get_workflows():
    rows = []
    for f in glob.glob(os.path.join(BASE_DIR, "workflows/*.md")):
        name, trigger, desc = parse_frontmatter(f)
        if name != "README":
            rows.append(rf"| `/{name}` | \\"{trigger}\\" | {desc} |")
    return sorted(rows)

def get_tools():
    rows = []
    for f in glob.glob(os.path.join(BASE_DIR, "tools/scripts/*")):
        if f.endswith('.py') or f.endswith('.sh'):
            name = os.path.basename(f)
            desc = "Script utility."
            try:
                with open(f, 'r') as file:
                    content = file.read(500)
                    doc_match = re.search(r'(\\"{3}|\\'\\'{3})([\\s\\S]*?)\\1', content)
                    if doc_match:
                         desc = doc_match.group(2).strip().replace('\\n', ' ')[:100]
            except: pass
            rows.append(rf"| `{name}` | Script | {desc} |")
    return sorted(rows)

def update_table(content, header, rows):
    if not rows: return content
    pattern = re.compile(rf'(### {header}[\\s\\S]*?\\| :--- \\|\\n)([\\s\\S]*?)(?=\\n\\n|\\n\\#)', re.MULTILINE)
    
    new_table = "\\n".join(rows)
    if pattern.search(content):
        return pattern.sub(rf'\\1{new_table}', content)
    else:
        print(f"Warning: Could not find table for {header}")
        return content

def update_agents_md():
    if not os.path.exists(AGENTS_FILE):
        print(f"Error: {AGENTS_FILE} not found.")
        return

    with open(AGENTS_FILE, 'r') as f:
        content = f.read()

    print("Syncing Skills...")
    content = update_table(content, "🧠 Core Skills", get_skills())
    
    print("Syncing Rules...")
    content = update_table(content, "🛡️ Active Rules", get_rules())
    
    print("Syncing Workflows...")
    content = update_table(content, "🔄 Standard Workflows", get_workflows())

    print("Syncing Tools...")
    content = update_table(content, "🛠️ Standard Tools", get_tools())

    with open(AGENTS_FILE, 'w') as f:
        f.write(content)
    print("✅ AGENTS.md updated successfully.")

if __name__ == "__main__":
    update_agents_md()
'''

LINT_AGENT_SETUP_PY = '''#!/usr/bin/env python3
"""
The Doctor 🩺
Validates the integrity of the .agent configuration.
"""
import os
import sys
import glob

BASE_DIR = ".agent"
REQUIRED_DIRS = ["skills", "tools", "rules", "workflows", "docs"]

def check_structure():
    errors = []
    for d in REQUIRED_DIRS:
        if not os.path.isdir(os.path.join(BASE_DIR, d)):
            errors.append(f"Missing directory: {d}")
    return errors

def validate_frontmatter(filepath, required_fields):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            parts = content.split('---')
            if len(parts) < 3:
                return f"Invalid YAML frontmatter: {filepath}"
            
            # Simple field check without yaml library
            for field in required_fields:
                if f"{field}:" not in parts[1]:
                    return f"Missing field '{field}' in {filepath}"
    except Exception as e:
        return f"Error parsing {filepath}: {e}"
    return None

def check_contents():
    errors = []
    
    # Skills
    for f in glob.glob(os.path.join(BASE_DIR, "skills/*/SKILL.md")):
        err = validate_frontmatter(f, ["name", "description", "trigger"])
        if err: errors.append(err)

    # Rules
    for f in glob.glob(os.path.join(BASE_DIR, "rules/*.md")):
        if not f.endswith("README.md"):
            err = validate_frontmatter(f, ["name", "trigger", "scope"])
            if err: errors.append(err)
            
    # Workflows
    for f in glob.glob(os.path.join(BASE_DIR, "workflows/*.md")):
        if not f.endswith("README.md"):
            err = validate_frontmatter(f, ["description", "trigger"])
            if err: errors.append(err)

    return errors

def main():
    print("🩺 Running Agent Doctor...")
    structure_errors = check_structure()
    content_errors = check_contents()
    
    all_errors = structure_errors + content_errors
    
    if all_errors:
        print("\\n❌ Found issues:")
        for e in all_errors:
            print(f" - {e}")
        sys.exit(1)
    else:
        print("\\n✅ System looks healthy!")
        sys.exit(0)

if __name__ == "__main__":
    main()
'''
