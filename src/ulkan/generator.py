from pathlib import Path

from .styles import console
from .templates import (  # noqa: F401 - templates is now a package
    # ADR Creator
    ADR_CREATOR_SKILL_MD,
    ADR_TEMPLATE_MD,
    # Root
    AGENTS_MD_TEMPLATE,
    ARCHITECTURE_TEMPLATE_MD,
    BUG_FIX_WORKFLOW,
    DECISIONS_README_TEMPLATE,
    DOCUMENTATION_CHECK_WORKFLOW,
    # Standard Workflows
    FEATURE_DEVELOPMENT_WORKFLOW,
    GUIDELINE_TEMPLATE_MD,
    # Guidelines Creator
    GUIDELINES_CREATOR_SKILL_MD,
    GUIDELINES_README_TEMPLATE,
    LINT_AGENT_SETUP_PY,
    MIGRATE_WORKFLOW,
    # Product Docs Creator
    PRODUCT_DOCS_CREATOR_SKILL_MD,
    PRODUCT_INCEPTION_WORKFLOW,
    PRODUCT_README_TEMPLATE,
    REFACTORING_WORKFLOW,
    RULE_TEMPLATE_MD,
    # Rules Creator
    RULES_CREATOR_SKILL_MD,
    RULES_README_TEMPLATE,
    SCRIPTS_README_TEMPLATE,
    # Skill Creator
    SKILL_CREATOR_SKILL_MD,
    SKILL_TEMPLATE_MD,
    # READMEs
    SKILLS_README_TEMPLATE,
    SPEC_TEMPLATE_MD,
    # Specs Creator
    SPECS_CREATOR_SKILL_MD,
    SPECS_README_TEMPLATE,
    # Scripts
    SYNC_AGENTS_DOCS_PY,
    TOOL_TEMPLATE_MD,
    # Tools Creator
    TOOLS_CREATOR_SKILL_MD,
    TOOLS_README_TEMPLATE,
    VISION_TEMPLATE_MD,
    WORKFLOW_TEMPLATE_MD,
    # Workflows Creator
    WORKFLOWS_CREATOR_SKILL_MD,
    WORKFLOWS_README_TEMPLATE,
)


def create_directory(path: Path) -> None:
    """Creates a directory if it doesn't exist."""
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, content: str, base_path: Path | None = None) -> bool:
    """Writes content to a file if it doesn't exist.

    Args:
        path: The file path to write to.
        content: The content to write.
        base_path: Optional base path for relative display in logs.

    Returns:
        True if file was created, False if it already existed.
    """
    if path.exists():
        # Show relative path for better context
        if base_path:
            display_path = path.relative_to(base_path)
        else:
            display_path = f"{path.parent.name}/{path.name}"
        console.print(f"[warning]  ⊘ Skipped: {display_path}[/warning]")
        return False

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


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
    write_file(agent_dir / "workflows" / "feat.md", FEATURE_DEVELOPMENT_WORKFLOW)
    write_file(agent_dir / "workflows" / "fix.md", BUG_FIX_WORKFLOW)
    write_file(agent_dir / "workflows" / "docs.md", DOCUMENTATION_CHECK_WORKFLOW)
    write_file(agent_dir / "workflows" / "build.md", PRODUCT_INCEPTION_WORKFLOW)
    write_file(agent_dir / "workflows" / "refactor.md", REFACTORING_WORKFLOW)
    write_file(agent_dir / "workflows" / "migrate.md", MIGRATE_WORKFLOW)

    # 13. Scripts
    scripts_dir = agent_dir / "tools" / "scripts"
    write_file(scripts_dir / "sync_agents_docs.py", SYNC_AGENTS_DOCS_PY)
    write_file(scripts_dir / "lint_agent_setup.py", LINT_AGENT_SETUP_PY)
