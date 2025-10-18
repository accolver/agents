# Agent Development Guide

This repository contains reusable OpenCode agent definitions (markdown files).
No build/test commands needed.

## Structure

- `agent/` - Agent definitions (subagents invoked with @agent-name)
- `command/` - Command definitions (slash commands like /test, /deploy)
- Each file is a standalone markdown document with YAML frontmatter

## Code Style

### Agent Files (.md in agent/)

- YAML frontmatter: description, mode: subagent, temperature (0.1-0.3), tools
  permissions
- Markdown body: Instructions, process steps, quality standards, examples
- Keep instructions focused and actionable
- Use clear section headers (##) for organization
- Include code examples in fenced blocks with language identifiers

### Naming Conventions

- Agent files: lowercase-with-hyphens.md (e.g., `feature-implementation.md`)
- Invoked with: `@agent-name` (e.g., `@feature-implementation`)
- Descriptive names matching their purpose

### Agent Configuration Standards

- Temperature: 0.1 (audit/review), 0.2 (implementation), 0.3 (research/creative)
- Tools: Grant minimum necessary permissions (read-only for auditors, full
  access for implementers)
- Description: Clear, concise summary of agent purpose for auto-invocation by
  primary agents
