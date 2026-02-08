# Product Vision: Ulkan

## 1. Mission Statement
To make "agent-ready" the default state for every software project, eliminating the friction between human developers and AI assistants.

## 2. The Problem
*   **Fragmentation**: Every developer configures their AI agent differently (system prompts, recommended extensions, ignored files).
*   **Context Loss**: AI agents often lack the "big picture" (architecture, conventions, business goals) leading to hallucinations or misaligned code.
*   **Maintenance Burden**: Keeping `CLAUDE.md`, `.cursorrules`, and custom instructions in sync is manual and error-prone.

## 3. The Solution: Ulkan
Ulkan is an **Agentic Scaffolding Tool** that provides a standardized, agent-agnostic interface for any codebase.

*   **Standardized Context**: A strictly defined `.agent/` directory structure acting as the Single Source of Truth (SSOT).
*   **Universal Compatibility**: Adapters that automatically generate configuration for specific agents (Claude, Gemini, Copilot, etc.) from the SSOT.
*   **Living Documentation**: CLI tools (`ulkan sync`, `ulkan build`) that keep documentation fresh and accurate.

## 4. Target Audience
*   **Software Engineers** adapting to AI-assisted workflows.
*   **Tech Leads** wanting to enforce consistency across team members' AI agents.
*   **maintainers** of open-source projects who want to make their code base easily understandable by AI contributors.

## 5. Core Values
*   **Zero Magic**: Everything is explicit files and folders.
*   **Agent Agnostic**: Don't lock into one specific AI vendor.
*   **Automated Maintenance**: If it can be scripted, it shouldn't be a wiki page.
