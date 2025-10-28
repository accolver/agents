# Build Scripts

## Overview

This directory contains build scripts that generate platform-specific agent and
command files from the source files in `agent/` and `command/`.

## build.py

The main build script that converts OpenCode-format source files into
platform-specific formats.

### Usage

```bash
# From repository root
python3 scripts/build.py

# Or using make
make build
```

### What It Does

1. **Reads source files** from `agent/` and `command/` directories (OpenCode
   format)
2. **Generates OpenCode files** in `build/opencode/` (preserves original format)
3. **Generates Claude Code files** in `build/claude/` (converts to Claude Code
   format)

### Format Conversions

#### Agent Files

**OpenCode format** (source):

```yaml
---
description: Reviews code for best practices
mode: subagent
temperature: 0.2
tools:
  read: true
  bash: true
  write: false
---
```

**Claude Code format** (generated):

```yaml
---
name: code-reviewer
description: Reviews code for best practices
tools: Read, Bash
model: inherit
---
```

#### Command Files

**OpenCode format** (source):

```yaml
---
description: Create a git commit
agent: build
---

Run git commands: !`git status`
```

**Claude Code format** (generated):

```yaml
---
description: Create a git commit
allowed-tools: Bash(git:*)
---

Run git commands: !`git status`
```

### Features

- **Tool mapping**: Converts OpenCode tool dict to Claude Code comma-separated
  list
- **Bash detection**: Automatically adds `allowed-tools` for commands with bash
  execution
- **Argument detection**: Adds `argument-hint` for commands using `$ARGUMENTS`
  or `$1`, `$2`, etc.
- **Name generation**: Extracts filename as `name` field for Claude Code agents

### Dependencies

- Python 3.6+
- PyYAML (install with `pip install pyyaml`)

### Output

```
build/
├── opencode/
│   ├── agent/       # 15 OpenCode-format agent files
│   └── command/     # 16 OpenCode-format command files
└── claude/
    ├── agents/      # 15 Claude Code-format agent files
    └── commands/    # 16 Claude Code-format command files
```

## Adding New Agents or Commands

1. Create your agent/command file in `agent/` or `command/` using **OpenCode
   format**
2. Run `make build` to generate platform-specific versions
3. Run `make install-opencode` or `make install-claude` to install

The build script automatically handles format conversion.

## Troubleshooting

### "Could not parse file, skipping"

The source file doesn't have valid YAML frontmatter. Ensure it starts with `---`
and has proper YAML syntax.

### "Module not found: yaml"

Install PyYAML:

```bash
pip install pyyaml
```

### Build files not updating

Clean and rebuild:

```bash
make clean
make build
```
