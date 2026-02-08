"""
Templates for the Ulkan CLI generator.

This package contains all file templates organized by category:
- agents: Root AGENTS.md manifest
- readme: README files for all directories
- skills: Skill creator templates (8 skills)
- workflows: Standard workflow templates (5 workflows)
- scripts: Python maintenance scripts (lint, sync)
"""

# Root manifest
from .agents import AGENTS_MD_TEMPLATE

# READMEs
from .readme import (
    DECISIONS_README_TEMPLATE,
    GUIDELINES_README_TEMPLATE,
    PRODUCT_README_TEMPLATE,
    RULES_README_TEMPLATE,
    SCRIPTS_README_TEMPLATE,
    SKILLS_README_TEMPLATE,
    SPECS_README_TEMPLATE,
    TOOLS_README_TEMPLATE,
    WORKFLOWS_README_TEMPLATE,
)

# Scripts
from .scripts import (
    LINT_AGENT_SETUP_PY,
    SYNC_AGENTS_DOCS_PY,
)

# Skills
from .skills import (
    # ADR Creator
    ADR_CREATOR_SKILL_MD,
    ADR_TEMPLATE_MD,
    ARCHITECTURE_TEMPLATE_MD,
    GUIDELINE_TEMPLATE_MD,
    # Guidelines Creator
    GUIDELINES_CREATOR_SKILL_MD,
    # Product Docs Creator
    PRODUCT_DOCS_CREATOR_SKILL_MD,
    RULE_TEMPLATE_MD,
    # Rules Creator
    RULES_CREATOR_SKILL_MD,
    # Skill Creator
    SKILL_CREATOR_SKILL_MD,
    SKILL_TEMPLATE_MD,
    SPEC_TEMPLATE_MD,
    # Specs Creator
    SPECS_CREATOR_SKILL_MD,
    TOOL_TEMPLATE_MD,
    # Tools Creator
    TOOLS_CREATOR_SKILL_MD,
    VISION_TEMPLATE_MD,
    WORKFLOW_TEMPLATE_MD,
    # Workflows Creator
    WORKFLOWS_CREATOR_SKILL_MD,
)

# Workflows
from .workflows import (
    BUG_FIX_WORKFLOW,
    DOCUMENTATION_CHECK_WORKFLOW,
    FEATURE_DEVELOPMENT_WORKFLOW,
    MIGRATE_WORKFLOW,
    PRODUCT_INCEPTION_WORKFLOW,
    REFACTORING_WORKFLOW,
)

__all__ = [
    # Root
    "AGENTS_MD_TEMPLATE",
    # READMEs
    "SKILLS_README_TEMPLATE",
    "TOOLS_README_TEMPLATE",
    "RULES_README_TEMPLATE",
    "WORKFLOWS_README_TEMPLATE",
    "GUIDELINES_README_TEMPLATE",
    "SPECS_README_TEMPLATE",
    "PRODUCT_README_TEMPLATE",
    "DECISIONS_README_TEMPLATE",
    "SCRIPTS_README_TEMPLATE",
    # Skill Creator
    "SKILL_CREATOR_SKILL_MD",
    "SKILL_TEMPLATE_MD",
    # Rules Creator
    "RULES_CREATOR_SKILL_MD",
    "RULE_TEMPLATE_MD",
    # Tools Creator
    "TOOLS_CREATOR_SKILL_MD",
    "TOOL_TEMPLATE_MD",
    # Specs Creator
    "SPECS_CREATOR_SKILL_MD",
    "SPEC_TEMPLATE_MD",
    # ADR Creator
    "ADR_CREATOR_SKILL_MD",
    "ADR_TEMPLATE_MD",
    # Product Docs Creator
    "PRODUCT_DOCS_CREATOR_SKILL_MD",
    "VISION_TEMPLATE_MD",
    "ARCHITECTURE_TEMPLATE_MD",
    # Guidelines Creator
    "GUIDELINES_CREATOR_SKILL_MD",
    "GUIDELINE_TEMPLATE_MD",
    # Workflows Creator
    "WORKFLOWS_CREATOR_SKILL_MD",
    "WORKFLOW_TEMPLATE_MD",
    # Workflows
    "FEATURE_DEVELOPMENT_WORKFLOW",
    "BUG_FIX_WORKFLOW",
    "DOCUMENTATION_CHECK_WORKFLOW",
    "PRODUCT_INCEPTION_WORKFLOW",
    "REFACTORING_WORKFLOW",
    "MIGRATE_WORKFLOW",
    # Scripts
    "SYNC_AGENTS_DOCS_PY",
    "LINT_AGENT_SETUP_PY",
]
