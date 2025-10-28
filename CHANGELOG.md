# Changelog

## [2.0.0] - 2025-10-28

### Added - Claude Code Support with Build System

This repository now supports both **OpenCode** and **Claude Code** through an
automated build system that generates platform-specific files from a single
source!

#### Build System

- **New `scripts/build.py`**: Automated build script that converts agent and
  command files between platform formats
- **New `scripts/check_deps.sh`**: Automatically checks and installs
  dependencies (PyYAML)
- **Platform-specific generation**: Automatically generates correct frontmatter
  for each platform
- **Single source of truth**: Maintain files in `agent/` and `command/`
  directories (OpenCode format)
- **Build directory**: Generated files in `build/opencode/` and `build/claude/`
  (not in git)

#### One Command Installation

```bash
git clone https://github.com/accolver/agent.git && cd agent && make
```

Just run `make` (or `make install-all`) to:

- ✅ Check for Python 3
- ✅ Auto-install PyYAML if needed
- ✅ Build platform-specific files
- ✅ Install for both OpenCode and Claude Code
- ✅ Show usage examples

#### Makefile Targets

- `make` or `make install-all` - Install everything (default)
- `make install-opencode` - Install for OpenCode only
- `make install-claude` - Install for Claude Code only
- `make build` - Build platform-specific files
- `make clean` - Remove build directory
- `make help` - Show available commands

#### How It Works

The build system solves the incompatibility between OpenCode and Claude Code
formats:

**OpenCode Format:**

```yaml
---
description: ...
mode: subagent
temperature: 0.2
tools:
  write: true
  read: true
---
```

**Claude Code Format (auto-generated):**

```yaml
---
name: agent-name
description: ...
tools: Write, Read
model: inherit
---
```

#### Key Features

1. **Automatic Conversion**: Build script reads OpenCode-format source files and
   generates platform-specific versions
2. **Tool Mapping**: Converts OpenCode tool permissions (dict) to Claude Code
   format (comma-separated list)
3. **Bash Command Detection**: Automatically adds `allowed-tools` to Claude Code
   commands that use bash
4. **Argument Detection**: Automatically adds `argument-hint` to commands with
   `$ARGUMENTS` or `$1`, `$2`, etc.

#### Documentation Updates

**README.md**

- Added "How It Works" section explaining build system
- Added platform comparison with format examples
- Updated installation instructions
- Added section documenting all 16 available commands
- Updated usage examples for both platforms

**Makefile**

- Completely rewritten to use build system
- Removed old `copy-*` targets
- All targets now run build script first
- Added `clean` target

#### Directory Structure

```
agent/               # Source files (OpenCode format)
command/             # Source files (OpenCode format)
scripts/build.py     # Build script
build/               # Generated files (not in git)
  ├── opencode/      # OpenCode-compatible files
  │   ├── agent/
  │   └── command/
  └── claude/        # Claude Code-compatible files
      ├── agents/
      └── commands/
```

### Technical Details

#### Directory Locations

| Platform        | Agents                                            | Commands                                              |
| --------------- | ------------------------------------------------- | ----------------------------------------------------- |
| **OpenCode**    | `~/.config/opencode/agent/` or `.opencode/agent/` | `~/.config/opencode/command/` or `.opencode/command/` |
| **Claude Code** | `~/.claude/agents/` or `.claude/agents/`          | `~/.claude/commands/` or `~/.claude/commands/`        |

#### Build Script Features

- Written in Python 3 with YAML parsing
- Converts tool permissions between formats
- Detects bash commands in command files
- Detects argument usage in command files
- Preserves all body content unchanged
- Handles all 15 agents and 16 commands

### Migration Guide

#### For Existing Users

If you previously installed agents/commands for OpenCode:

```bash
cd agent
git pull
make install-opencode  # Rebuilds and reinstalls
```

#### For New Claude Code Users

```bash
git clone https://github.com/accolver/agent.git
cd agent
make install-claude
```

#### For Users of Both Platforms

```bash
git clone https://github.com/accolver/agent.git
cd agent
make install-all
```

### What Works Where

| Feature                    | OpenCode                  | Claude Code                              |
| -------------------------- | ------------------------- | ---------------------------------------- |
| Agent invocation           | `@agent-name`             | Automatic delegation or explicit request |
| Command invocation         | `/command-name`           | `/command-name`                          |
| Bash execution in commands | ✅                        | ✅ (with `allowed-tools`)                |
| Tool restrictions          | Per-agent via frontmatter | Per-agent via frontmatter                |
| Project-level configs      | ✅                        | ✅                                       |
| User-level configs         | ✅                        | ✅                                       |

### Breaking Changes

- **Source files must be in OpenCode format**: The `agent/` and `command/`
  directories use OpenCode's YAML format
- **Build step required**: Must run `make build` or use install targets (happens
  automatically)
- **Previous generated files removed**: Old attempts at dual-format files have
  been replaced with build system

### Backward Compatibility

- Source files remain in OpenCode format (no changes needed)
- Installation process improved (now uses build system)
- All existing functionality preserved
- No breaking changes for end users (installation commands work the same)

### Resources

- [OpenCode Documentation](https://opencode.ai/docs/)
- [OpenCode Agents Guide](https://opencode.ai/docs/agents/#markdown)
- [Claude Code Subagents Guide](https://docs.claude.com/en/docs/claude-code/sub-agents)
- [Claude Code Slash Commands Guide](https://docs.claude.com/en/docs/claude-code/slash-commands)
