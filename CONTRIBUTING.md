# Contributing

Thank you for your interest in contributing to this agent and command
collection!

## Development Setup

1. **Clone and setup**
   ```bash
   git clone https://github.com/accolver/agent.git
   cd agent
   make  # Installs dependencies and builds everything
   ```

That's it! The `make` command automatically:

- Checks for Python 3
- Installs PyYAML if needed
- Builds platform-specific files
- Installs for both platforms

## Repository Structure

```
agent/               # Source agent files (OpenCode format)
command/             # Source command files (OpenCode format)
scripts/
  └── build.py       # Build script for generating platform files
build/               # Generated files (not in git)
  ├── opencode/      # OpenCode-compatible files
  └── claude/        # Claude Code-compatible files
```

## Adding a New Agent

1. **Create the agent file** in `agent/` using OpenCode format:

   ```yaml
   ---
   description: Brief description of when to use this agent
   mode: subagent
   temperature: 0.2
   tools:
     write: true
     read: true
     bash: false
   ---

   Your agent's system prompt goes here.
   Include detailed instructions on what the agent should do.
   ```

2. **Test the build**:
   ```bash
   make build
   ```

3. **Verify the generated files**:
   ```bash
   # Check OpenCode version
   cat build/opencode/agent/your-agent.md

   # Check Claude Code version
   cat build/claude/agents/your-agent.md
   ```

4. **Test installation**:
   ```bash
   make install-opencode
   # or
   make install-claude
   ```

## Adding a New Command

1. **Create the command file** in `command/` using OpenCode format:

   ```yaml
   ---
   description: Brief description of what this command does
   agent: build
   ---

   Your command prompt goes here.

   Use !`bash commands` for executing shell commands.
   Use $ARGUMENTS or $1, $2 for command arguments.
   ```

2. **Follow the same build and test process** as agents.

## File Format Requirements

### Source Files (OpenCode Format)

All source files in `agent/` and `command/` must use OpenCode format:

**Agents:**

```yaml
---
description: Required description
mode: subagent
temperature: 0.1-0.3
tools:
  tool_name: true/false
---
```

**Commands:**

```yaml
---
description: Required description
agent: build|plan|general
subtask: true  # optional
---
```

The build script automatically converts these to Claude Code format.

## Build System

The `scripts/build.py` script handles format conversion:

- **Agents**: Adds `name:` and `model:` fields, converts tools to
  comma-separated list
- **Commands**: Adds `allowed-tools:` for bash commands, `argument-hint:` for
  arguments
- **Both**: Preserves body content unchanged

### Testing Your Changes

1. **Build**: `make build`
2. **Check generated files**: Look in `build/opencode/` and `build/claude/`
3. **Install locally**: `make install-opencode` or `make install-claude`
4. **Test with actual CLI**: Try using your agent/command

## Pull Request Guidelines

1. **Keep source files in OpenCode format** - The build script handles
   conversions
2. **Test both platforms** - Verify generated files work with OpenCode and
   Claude Code
3. **Update documentation** - Add your agent/command to README.md
4. **Follow naming conventions**:
   - Agent files: `lowercase-with-hyphens.md`
   - Agent names: Match the filename
   - Commands: Same naming as agents

5. **Write clear descriptions**:
   - Agents: Explain when the agent should be invoked
   - Commands: Explain what the command does
   - Use actionable language

6. **Include examples** in your PR description:
   - Show how to invoke the agent/command
   - Provide example use cases
   - Show expected output if relevant

## Code Style

### Agent Prompts

- Be specific and detailed
- Include step-by-step process
- Specify quality standards
- Provide examples where helpful
- Use clear section headers (##)

### Command Prompts

- Be concise and actionable
- Use bash execution (!`) where needed
- Support arguments if applicable
- Provide context through bash commands

### Tool Permissions

- **Read-only agents**: Only enable `read`, `grep`, `glob`, `bash` (for safe
  commands)
- **Implementation agents**: Enable `write`, `edit`, and other modification
  tools
- **Research agents**: Enable `webfetch` for external information

## Quality Standards

Before submitting:

- [ ] Source files are in OpenCode format
- [ ] Build script runs without errors
- [ ] Generated files have correct format for both platforms
- [ ] Agent/command description is clear and specific
- [ ] Tool permissions are appropriate for the task
- [ ] Temperature setting matches the agent's purpose
- [ ] Documentation is updated in README.md
- [ ] CHANGELOG.md is updated if adding new features

## Questions?

- Open an issue for questions about contributing
- Check existing agents/commands for examples
- Read the documentation in `scripts/README.md`

## License

By contributing, you agree that your contributions will be licensed under the
same license as the project.
