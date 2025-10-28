# Technical Documentation

## Problem Statement

OpenCode and Claude Code both support custom agents and commands, but they use
**incompatible file formats** for frontmatter:

### OpenCode Format

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

### Claude Code Format

```yaml
---
name: code-reviewer
description: Reviews code for best practices
tools: Read, Bash
model: inherit
---
```

Key differences:

- **Field names**: `mode` vs `name`, `model` field only in Claude Code
- **Tools format**: YAML dict vs comma-separated string
- **Tool names**: lowercase vs TitleCase
- **Directory names**: `agent/` vs `agents/`, `command/` vs `commands/`

## Solution: Build System

Rather than maintaining duplicate files or trying to create a "universal"
format, we use a build system that:

1. **Single source of truth**: Maintain files in OpenCode format (the original
   format)
2. **Generate on demand**: Convert to platform-specific formats during
   installation
3. **No duplication**: Generated files are in `build/` and excluded from git

## Architecture

```
┌─────────────┐
│   agent/    │  Source files (OpenCode format)
│  command/   │  Maintained by contributors
└──────┬──────┘
       │
       ├─────────────┐
       │             │
       v             v
┌─────────────┐  ┌──────────────┐
│    Build    │  │    Build     │
│   OpenCode  │  │ Claude Code  │
└──────┬──────┘  └──────┬───────┘
       │                │
       v                v
┌──────────────┐ ┌─────────────────┐
│build/opencode│ │  build/claude   │
│  ├─agent/    │ │  ├─agents/      │
│  └─command/  │ │  └─commands/    │
└──────┬───────┘ └──────┬──────────┘
       │                │
       v                v
┌──────────────┐ ┌─────────────────┐
│~/.config/    │ │   ~/.claude/    │
│  opencode/   │ │                 │
└──────────────┘ └─────────────────┘
```

## Build Script (scripts/build.py)

### Core Functions

#### 1. `parse_opencode_frontmatter(content)`

Parses YAML frontmatter from markdown files using regex and PyYAML.

#### 2. `tools_dict_to_claude_list(tools_dict)`

Converts OpenCode tool permissions to Claude Code format:

```python
{
    'read': True,
    'write': True,
    'bash': False
}
# becomes
"Read, Write"
```

#### 3. `build_opencode_agent(config, body, filename)`

Preserves OpenCode format (passthrough for agents, minimal changes for
commands).

#### 4. `build_claude_agent(config, body, filename)`

Converts to Claude Code format:

- Extracts `name` from filename
- Converts `tools` dict to comma-separated list
- Adds `model: inherit` field
- Removes `mode` and `temperature` fields

#### 5. `build_claude_command(config, body, filename)`

Generates Claude Code command format:

- Detects bash commands (`` !`command` ``) and adds `allowed-tools`
- Detects arguments (`$ARGUMENTS`, `$1`, `$2`) and adds `argument-hint`
- Preserves `description` field

### Tool Mapping

```python
tool_mapping = {
    'write': 'Write',
    'edit': 'Edit',
    'read': 'Read',
    'bash': 'Bash',
    'grep': 'Grep',
    'glob': 'Glob',
    'webfetch': 'WebFetch',
    'list': 'List',
    'task': 'Task'
}
```

### Bash Command Detection

For commands, the build script scans the body for bash execution patterns:

```markdown
!`git status` !`npm test`
```

It extracts the base command (`git`, `npm`) and generates:

```yaml
allowed-tools: Bash(git:*), Bash(npm:*)
```

### Argument Detection

Scans for argument patterns:

- `$ARGUMENTS` - All arguments as single string
- `$1`, `$2`, `$3` - Positional arguments

If found, adds:

```yaml
argument-hint: [args]
```

## Makefile Integration

The Makefile provides convenient targets:

```makefile
build:
    python3 scripts/build.py

install-opencode: build
    # Copy build/opencode/ to ~/.config/opencode/

install-claude: build
    # Copy build/claude/ to ~/.claude/

install-all: install-opencode install-claude
    # Install for both platforms
```

## Testing Strategy

### Unit Testing (Manual)

1. Verify source file parsing
2. Check tool conversion
3. Validate generated frontmatter
4. Ensure body content preserved

### Integration Testing (via Makefile)

1. Run `make build`
2. Check generated files exist
3. Verify format correctness
4. Test actual installation

### End-to-End Testing

1. Install for OpenCode: `make install-opencode`
2. Test with `opencode` CLI
3. Install for Claude Code: `make install-claude`
4. Test with `claude` CLI

## File Format Validation

### OpenCode Validation

- Must have `description` field
- Must have `mode: subagent` for agents
- Tools must be dict with boolean values
- Temperature should be 0.1-0.3

### Claude Code Validation

- Must have `name` field (extracted from filename)
- Must have `description` field
- Tools must be comma-separated string (if present)
- Must have `model:` field (set to 'inherit')

## Error Handling

### Parse Errors

If YAML frontmatter is invalid:

```
Warning: Could not parse {file}, skipping
```

### Missing Dependencies

If PyYAML not installed:

```
ModuleNotFoundError: No module named 'yaml'
```

Solution: `pip install pyyaml`

### Build Failures

Build script creates directories automatically, so failures are rare. Check:

1. Python version (needs 3.6+)
2. File permissions
3. YAML syntax in source files

## Performance

Build time for current repository (15 agents + 16 commands):

- **Parse & Convert**: ~0.1s
- **Write files**: ~0.05s
- **Total**: < 0.2s

Very fast, can be run on every install without noticeable delay.

## Future Enhancements

### Potential Improvements

1. **Validation**: Add schema validation for source files
2. **Tests**: Add automated tests for build script
3. **Watch mode**: Auto-rebuild on file changes
4. **Linting**: Check for common mistakes in agent/command prompts
5. **Templates**: Provide agent/command templates

### Adding New Platforms

To support a third platform:

1. Add `build_{platform}_agent()` function
2. Add `build_{platform}_command()` function
3. Update `process_agents()` and `process_commands()`
4. Add Makefile target: `install-{platform}`

## Dependencies

### Runtime

- Python 3.6+
- PyYAML

### Development

- git
- make
- Text editor

## Security Considerations

### Tool Permissions

Build script preserves tool restrictions from source files. Review each agent's
tools carefully:

- Read-only agents should not have `write`, `edit`
- Sensitive operations should require `bash` permission
- External access requires `webfetch`

### Bash Commands in Commands

Commands with bash execution (`` !` ` ``) automatically get `allowed-tools`.
Review these carefully as they can execute arbitrary commands.

### Source File Trust

Only accept source files from trusted contributors. All agents and commands
execute with the user's permissions.

## Maintenance

### Adding Agents

1. Create source file in `agent/`
2. Use OpenCode format
3. Run `make build` to test
4. Submit PR with updated README

### Modifying Build Script

1. Test with current files first
2. Ensure backward compatibility
3. Update TECHNICAL.md
4. Add examples of new conversions

### Updating for Platform Changes

If OpenCode or Claude Code changes their format:

1. Update relevant `build_{platform}_*()` functions
2. Test with all existing files
3. Update documentation
4. Release new version

## Troubleshooting

### "Build failed"

- Check Python version: `python3 --version`
- Install PyYAML: `pip install pyyaml`
- Check file permissions

### "Agent not found"

- Run `make install-{platform}` again
- Check correct directory: `~/.config/opencode/` or `~/.claude/`
- Verify file was generated: `ls build/{platform}/`

### "Invalid config"

- Check source file YAML syntax
- Ensure frontmatter starts/ends with `---`
- Validate YAML online

### "Tools not working"

- Check generated file: `cat ~/.config/opencode/agent/{name}.md`
- Verify tools are correctly formatted
- For Claude Code: tools should be comma-separated
- For OpenCode: tools should be YAML dict
