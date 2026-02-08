import os
from pathlib import Path
from .templates import (
    # Root
    AGENTS_MD_TEMPLATE,
    # READMEs
    SKILLS_README_TEMPLATE,
    TOOLS_README_TEMPLATE,
    RULES_README_TEMPLATE,
    WORKFLOWS_README_TEMPLATE,
    GUIDELINES_README_TEMPLATE,
    SPECS_README_TEMPLATE,
    PRODUCT_README_TEMPLATE,
    DECISIONS_README_TEMPLATE,
    SCRIPTS_README_TEMPLATE,
    # Skill Creator
    SKILL_CREATOR_SKILL_MD,
    SKILL_TEMPLATE_MD,
    # Rules Creator
    RULES_CREATOR_SKILL_MD,
    RULE_TEMPLATE_MD,
    # Tools Creator
    TOOLS_CREATOR_SKILL_MD,
    TOOL_TEMPLATE_MD,
    # Specs Creator
    SPECS_CREATOR_SKILL_MD,
    SPEC_TEMPLATE_MD,
    # ADR Creator
    ADR_CREATOR_SKILL_MD,
    ADR_TEMPLATE_MD,
    # Product Docs Creator
    PRODUCT_DOCS_CREATOR_SKILL_MD,
    VISION_TEMPLATE_MD,
    ARCHITECTURE_TEMPLATE_MD,
    # Guidelines Creator
    GUIDELINES_CREATOR_SKILL_MD,
    GUIDELINE_TEMPLATE_MD,
    # Workflows Creator
    WORKFLOWS_CREATOR_SKILL_MD,
    WORKFLOW_TEMPLATE_MD,
    # Standard Workflows
    FEATURE_DEVELOPMENT_WORKFLOW,
    BUG_FIX_WORKFLOW,
    DOCUMENTATION_CHECK_WORKFLOW,
    PRODUCT_INCEPTION_WORKFLOW,
    REFACTORING_WORKFLOW,
    # Scripts
    SYNC_AGENTS_DOCS_PY,
    LINT_AGENT_SETUP_PY,
)


def create_directory(path: Path) -> None:
    """Creates a directory if it doesn't exist."""
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, content: str) -> None:
    """Writes content to a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_project(base_path: Path) -> None:
    """Generates the agentic project structure.

    Args:
        base_path: The root directory where the project will be initialized.
    """

    # 1. Root Manifest (AGENTS.md)
    write_file(base_path / "AGENTS.md", AGENTS_MD_TEMPLATE)

    # 2. Core Directories
    agent_dir = base_path / ".agent"
    create_directory(agent_dir / "skills")
    create_directory(agent_dir / "tools" / "scripts")
    create_directory(agent_dir / "tools" / "mcp")
    create_directory(agent_dir / "tools" / "utils")
    create_directory(agent_dir / "rules")
    create_directory(agent_dir / "workflows")

    create_directory(agent_dir / "docs" / "product")
    create_directory(agent_dir / "docs" / "guidelines")
    create_directory(agent_dir / "docs" / "specs")
    create_directory(agent_dir / "docs" / "decisions")

    # 3. READMEs
    write_file(agent_dir / "skills" / "README.md", SKILLS_README_TEMPLATE)
    write_file(agent_dir / "tools" / "README.md", TOOLS_README_TEMPLATE)
    write_file(agent_dir / "tools" / "scripts" / "README.md", SCRIPTS_README_TEMPLATE)
    write_file(agent_dir / "rules" / "README.md", RULES_README_TEMPLATE)
    write_file(agent_dir / "workflows" / "README.md", WORKFLOWS_README_TEMPLATE)
    write_file(
        agent_dir / "docs" / "guidelines" / "README.md", GUIDELINES_README_TEMPLATE
    )
    write_file(agent_dir / "docs" / "specs" / "README.md", SPECS_README_TEMPLATE)
    write_file(agent_dir / "docs" / "product" / "README.md", PRODUCT_README_TEMPLATE)
    write_file(
        agent_dir / "docs" / "decisions" / "README.md", DECISIONS_README_TEMPLATE
    )

    # 4. Skill Creator
    skill_creator_dir = agent_dir / "skills" / "skill-creator"
    create_directory(skill_creator_dir / "assets")
    write_file(skill_creator_dir / "SKILL.md", SKILL_CREATOR_SKILL_MD)
    write_file(skill_creator_dir / "assets" / "SKILL-TEMPLATE.md", SKILL_TEMPLATE_MD)

    # 5. Rules Creator
    rules_creator_dir = agent_dir / "skills" / "rules-creator"
    create_directory(rules_creator_dir / "assets")
    write_file(rules_creator_dir / "SKILL.md", RULES_CREATOR_SKILL_MD)
    write_file(rules_creator_dir / "assets" / "RULE-TEMPLATE.md", RULE_TEMPLATE_MD)

    # 6. Tools Creator
    tools_creator_dir = agent_dir / "skills" / "tools-creator"
    create_directory(tools_creator_dir / "assets")
    write_file(tools_creator_dir / "SKILL.md", TOOLS_CREATOR_SKILL_MD)
    write_file(tools_creator_dir / "assets" / "TOOL-TEMPLATE.md", TOOL_TEMPLATE_MD)

    # 7. Specs Creator
    specs_creator_dir = agent_dir / "skills" / "specs-creator"
    create_directory(specs_creator_dir / "assets")
    write_file(specs_creator_dir / "SKILL.md", SPECS_CREATOR_SKILL_MD)
    write_file(specs_creator_dir / "assets" / "SPEC-TEMPLATE.md", SPEC_TEMPLATE_MD)

    # 8. ADR Creator
    adr_creator_dir = agent_dir / "skills" / "adr-creator"
    create_directory(adr_creator_dir / "assets")
    write_file(adr_creator_dir / "SKILL.md", ADR_CREATOR_SKILL_MD)
    write_file(adr_creator_dir / "assets" / "ADR-TEMPLATE.md", ADR_TEMPLATE_MD)

    # 9. Product Docs Creator
    product_docs_dir = agent_dir / "skills" / "product-docs-creator"
    create_directory(product_docs_dir / "assets")
    write_file(product_docs_dir / "SKILL.md", PRODUCT_DOCS_CREATOR_SKILL_MD)
    write_file(product_docs_dir / "assets" / "VISION-TEMPLATE.md", VISION_TEMPLATE_MD)
    write_file(
        product_docs_dir / "assets" / "ARCHITECTURE-TEMPLATE.md",
        ARCHITECTURE_TEMPLATE_MD,
    )

    # 10. Guidelines Creator
    guidelines_creator_dir = agent_dir / "skills" / "guidelines-creator"
    create_directory(guidelines_creator_dir / "assets")
    write_file(guidelines_creator_dir / "SKILL.md", GUIDELINES_CREATOR_SKILL_MD)
    write_file(
        guidelines_creator_dir / "assets" / "GUIDELINE-TEMPLATE.md",
        GUIDELINE_TEMPLATE_MD,
    )

    # 11. Workflows Creator
    workflows_creator_dir = agent_dir / "skills" / "workflows-creator"
    create_directory(workflows_creator_dir / "assets")
    write_file(workflows_creator_dir / "SKILL.md", WORKFLOWS_CREATOR_SKILL_MD)
    write_file(
        workflows_creator_dir / "assets" / "WORKFLOW-TEMPLATE.md", WORKFLOW_TEMPLATE_MD
    )

    # 12. Standard Workflows
    write_file(
        agent_dir / "workflows" / "feature-development.md", FEATURE_DEVELOPMENT_WORKFLOW
    )
    write_file(agent_dir / "workflows" / "bug-fix.md", BUG_FIX_WORKFLOW)
    write_file(
        agent_dir / "workflows" / "documentation-check.md", DOCUMENTATION_CHECK_WORKFLOW
    )
    write_file(
        agent_dir / "workflows" / "product-inception.md", PRODUCT_INCEPTION_WORKFLOW
    )
    write_file(agent_dir / "workflows" / "refactoring.md", REFACTORING_WORKFLOW)

    # 13. Scripts
    scripts_dir = agent_dir / "tools" / "scripts"
    write_file(scripts_dir / "sync_agents_docs.py", SYNC_AGENTS_DOCS_PY)
    write_file(scripts_dir / "lint_agent_setup.py", LINT_AGENT_SETUP_PY)
