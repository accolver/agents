# Installation Guide

## Quick Install (Recommended)

```bash
git clone https://github.com/accolver/agent.git && cd agent && make
```

**That's it!** This single command:

1. Clones the repository
2. Checks for Python 3 (shows clear error if missing)
3. Auto-installs PyYAML if needed
4. Builds platform-specific files
5. Installs for both OpenCode and Claude Code
6. Shows you how to use them

## What Gets Installed

### Agents (15 total)

Specialized AI assistants for different tasks:

- `@research` - Technical research and comparisons
- `@testing` - Comprehensive test suites
- `@security-audit` - Security vulnerability scanning
- `@code-reviewer` - Code quality reviews
- `@documentation` - Technical documentation
- `@api-design` - API architecture design
- `@database-design` - Database schema design
- `@feature-implementation` - Backend logic
- `@component-implementation` - UI components
- `@prd` - Product requirements documents
- `@infrastructure` - Build systems and tooling
- `@devops` - Deployment and CI/CD
- `@polish` - Performance optimization
- `@quality` - Quality assurance
- `@refactoring` - Code improvement

### Commands (16 total)

Quick slash commands for common tasks:

- `/commit` - Create git commits
- `/pr` - Create pull requests
- `/test` - Run tests
- `/review` - Code review
- `/deploy` - Deploy to production
- `/debug` - Debug issues
- `/fix` - Fix bugs
- `/security` - Security audit
- `/optimize` - Performance tuning
- `/refactor` - Code refactoring
- `/docs` - Documentation
- `/api` - API design
- `/db` - Database design
- `/setup` - Environment setup
- `/clean` - Code cleanup

## Installation Locations

### OpenCode

- Agents: `~/.config/opencode/agent/`
- Commands: `~/.config/opencode/command/`

### Claude Code

- Agents: `~/.claude/agents/`
- Commands: `~/.claude/commands/`

## Platform-Specific Install

If you only use one platform:

```bash
# OpenCode only
git clone https://github.com/accolver/agent.git
cd agent
make install-opencode

# Claude Code only
git clone https://github.com/accolver/agent.git
cd agent
make install-claude
```

## Updating

To get the latest agents and commands:

```bash
cd agent
git pull
make
```

## Uninstalling

To remove all agents and commands:

```bash
# OpenCode
rm -rf ~/.config/opencode/agent/*.md
rm -rf ~/.config/opencode/command/*.md

# Claude Code
rm -rf ~/.claude/agents/*.md
rm -rf ~/.claude/commands/*.md
```

## Project-Level Installation

To install for a specific project instead of globally:

```bash
cd your-project
git clone https://github.com/accolver/agent.git /tmp/agents
cd /tmp/agents
make build

# For OpenCode
mkdir -p .opencode/agent .opencode/command
cp build/opencode/agent/*.md .opencode/agent/
cp build/opencode/command/*.md .opencode/command/

# For Claude Code
mkdir -p .claude/agents .claude/commands
cp build/claude/agents/*.md .claude/agents/
cp build/claude/commands/*.md .claude/commands/

# Cleanup
cd your-project
rm -rf /tmp/agents
```

## Troubleshooting

### Python Not Found

**Error:** "Python 3 is not installed"

**Solution:** Install Python 3 from
[python.org](https://www.python.org/downloads/)

**Verify:**

```bash
python3 --version
```

### PyYAML Install Failed

**Error:** "Failed to install PyYAML"

**Solution:** Install manually:

```bash
pip3 install pyyaml
# or
pip3 install --user pyyaml
```

### Make Command Not Found

**Error:** "command not found: make"

**Solutions:**

- **macOS:** Install Xcode Command Line Tools
  ```bash
  xcode-select --install
  ```
- **Linux:** Install build-essential
  ```bash
  sudo apt-get install build-essential
  ```
- **Windows:** Use WSL (Windows Subsystem for Linux) or install Make for Windows

### Invalid Config (OpenCode)

**Error:** "Config file at ... is invalid"

**Solution:** Rebuild and reinstall:

```bash
cd agent
make clean
make install-opencode
```

### Agents Not Showing Up

**Check installation:**

```bash
# OpenCode
ls ~/.config/opencode/agent/

# Claude Code
ls ~/.claude/agents/
```

**If empty, reinstall:**

```bash
cd agent
make clean
make
```

**Restart your editor/terminal** after installation.

### Permission Denied

**Error:** Permission denied when copying files

**Solution:** The install script uses `~/.config/` and `~/.claude/` which should
be user-writable. If you get permission errors:

```bash
# Fix permissions
chmod -R u+w ~/.config/opencode/
chmod -R u+w ~/.claude/

# Retry installation
make
```

## Verification

After installation, verify it worked:

### OpenCode

```bash
ls ~/.config/opencode/agent/ | wc -l  # Should show 15
ls ~/.config/opencode/command/ | wc -l  # Should show 16
```

### Claude Code

```bash
ls ~/.claude/agents/ | wc -l  # Should show 15
ls ~/.claude/commands/ | wc -l  # Should show 16
```

### Test Usage

**OpenCode:**

```bash
opencode
# Try: @research What are the best practices for API design?
# Try: /commit
```

**Claude Code:**

```bash
claude
# Try: Use the research subagent to compare state management options
# Try: /commit
```

## Advanced

### Custom Build

If you want to modify agents before installing:

```bash
cd agent
# Edit files in agent/ or command/
make build  # Just build, don't install
# Check generated files in build/
make install-all  # Install when ready
```

### Single Agent Install

To install just one agent:

```bash
cd agent
make build
cp build/opencode/agent/testing.md ~/.config/opencode/agent/
cp build/claude/agents/testing.md ~/.claude/agents/
```

## Getting Help

- **Documentation:** See [README.md](README.md)
- **Technical Details:** See [TECHNICAL.md](TECHNICAL.md)
- **Contributing:** See [CONTRIBUTING.md](CONTRIBUTING.md)
- **Issues:** [GitHub Issues](https://github.com/accolver/agent/issues)

## Next Steps

After installation:

1. **Try an agent:**
   - OpenCode: `@research Compare React vs Vue`
   - Claude Code: "Use the research subagent to compare React vs Vue"

2. **Try a command:**
   - Both platforms: `/commit` to create a git commit

3. **Read the docs:**
   - [README.md](README.md) for full agent and command list
   - Platform docs: [OpenCode](https://opencode.ai/docs/) |
     [Claude Code](https://docs.claude.com/en/docs/claude-code/)

4. **Customize:**
   - Edit source files in `agent/` or `command/`
   - Run `make` to rebuild and reinstall
