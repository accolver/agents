# AI Agent & Command Collection

A comprehensive collection of specialized AI agents and custom commands for the
complete software development lifecycle. Works with both
[OpenCode](https://opencode.ai) and
[Claude Code](https://docs.claude.com/en/docs/claude-code).

## ⚡ Quick Start

```bash
git clone https://github.com/accolver/agent.git && cd agent && make
```

That's it! One command installs everything for both platforms.

## 📋 Overview

These agents and commands are designed to be **reusable across any project** and
cover everything from initial research and planning through to deployment and
maintenance.

### What's Included

- **Agents**: Specialized subagents that can be automatically delegated to or
  explicitly invoked
- **Commands**: Custom slash commands for frequently-used prompts and workflows

### Compatibility

This collection works with both:

- **OpenCode**: Invoke agents with `@agent-name`, use commands with
  `/command-name`
- **Claude Code**: Automatically delegated or explicitly invoked agents, custom
  slash commands

Both systems use the same file format (Markdown with YAML frontmatter), making
these agents and commands fully portable between platforms.

### Key Features

- **Cross-platform**: Works with both OpenCode and Claude Code
- **15 specialized agents**: From research to deployment
- **16 custom commands**: Common workflows like `/commit`, `/test`, `/deploy`
- **Easy installation**: Simple `make` commands for setup
- **Customizable**: Edit any agent or command to fit your needs
- **Project or user-level**: Install globally or per-project

## 🚀 Installation

### One Command Install (Recommended)

```bash
git clone https://github.com/accolver/agent.git && cd agent && make
```

That's it! This single command will:

- ✅ Check for Python 3 (shows error if not installed)
- ✅ Auto-install PyYAML dependency if needed
- ✅ Build platform-specific files
- ✅ Install for **both** OpenCode and Claude Code
- ✅ Show you usage examples

**What you get:**

- 15 specialized agents (research, testing, security, documentation, deployment,
  etc.)
- 16 custom commands (`/commit`, `/test`, `/review`, `/deploy`, `/security`,
  etc.)

### Platform-Specific Install

If you only use one platform:

```bash
# OpenCode only
git clone https://github.com/accolver/agent.git && cd agent && make install-opencode

# Claude Code only
git clone https://github.com/accolver/agent.git && cd agent && make install-claude
```

### Prerequisites

The install process **automatically handles dependencies**, but if you prefer to
install manually:

- Python 3.6+ (required)
- PyYAML (auto-installed if missing)

### How It Works

The repository structure:

- `agent/` - Source agent files (OpenCode format)
- `command/` - Source command files (OpenCode format)
- `scripts/build.py` - Build script that generates platform-specific files
- `build/` - Generated platform-specific files (not in git)
  - `build/opencode/` - OpenCode-compatible files
  - `build/claude/` - Claude Code-compatible files

When you run `make install-*`, the build script:

1. Reads the source files from `agent/` and `command/`
2. Generates platform-specific versions with correct frontmatter
3. Installs them to the appropriate locations

### Project-Level Installation

To install agents and commands for a specific project instead of globally:

```bash
# In your project directory
cd your-project

# Clone to a temporary location and run project install
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

# Clean up
cd your-project
rm -rf /tmp/agents
```

### Installing Individual Agents or Commands

To install just one or two agents instead of all of them:

```bash
# Clone and build
git clone https://github.com/accolver/agent.git /tmp/agents
cd /tmp/agents
make build

# Copy specific agents
cp build/opencode/agent/research.md ~/.config/opencode/agent/
cp build/claude/agents/testing.md ~/.claude/agents/

# Clean up
rm -rf /tmp/agents
```

### Updating Agents and Commands

To update to the latest version:

```bash
cd agent
git pull
make
```

### Troubleshooting

**"Python 3 is not installed"**

- Install Python from [python.org](https://www.python.org/downloads/)
- Verify: `python3 --version`

**"Failed to install PyYAML"**

- Install manually: `pip3 install pyyaml`
- Or with user flag: `pip3 install --user pyyaml`

**"Config file is invalid" (OpenCode)**

- The build system handles this automatically now
- If you see this, run: `make clean && make install-opencode`

**Agents not showing up**

- Check installation: `ls ~/.config/opencode/agent/` or `ls ~/.claude/agents/`
- Reinstall: `make clean && make`
- Restart your IDE or terminal

**"Command not found: make"**

- macOS: Install Xcode Command Line Tools: `xcode-select --install`
- Linux: Install build-essential: `sudo apt-get install build-essential`
- Windows: Use WSL or install Make for Windows

## 💬 Platform Differences

OpenCode and Claude Code have different file format requirements, which is why
this repository uses a build system to generate platform-specific files:

| Feature              | OpenCode                                              | Claude Code                                     |
| -------------------- | ----------------------------------------------------- | ----------------------------------------------- |
| **Agents**           | Invoked with `@agent-name`                            | Automatically delegated or explicitly invoked   |
| **Agent location**   | `.opencode/agent/` or `~/.config/opencode/agent/`     | `.claude/agents/` or `~/.claude/agents/`        |
| **Commands**         | Invoked with `/command-name`                          | Invoked with `/command-name`                    |
| **Command location** | `.opencode/command/` or `~/.config/opencode/command/` | `.claude/commands/` or `~/.claude/commands/`    |
| **File format**      | YAML with nested `tools:` dict                        | YAML with comma-separated `tools:` string       |
| **Agent fields**     | `description`, `mode`, `temperature`, `tools`         | `name`, `description`, `tools`, `model`         |
| **Command fields**   | `description`, `agent`, `subtask`                     | `description`, `allowed-tools`, `argument-hint` |
| **Management UI**    | Via configuration files                               | `/agents` command for interactive management    |

The build script automatically converts between these formats so you only
maintain one set of source files.

### Format Examples

**OpenCode Agent Format:**

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

**Claude Code Agent Format (auto-generated):**

```yaml
---
name: code-reviewer
description: Reviews code for best practices
tools: Read, Bash
model: inherit
---
```

## 📜 Available Commands

Custom slash commands are available in the `command/` directory. These are
frequently-used prompts that can be invoked with `/command-name`.

### Core Development Commands

- `/commit` - Review changes and create a git commit
- `/pr` - Create a pull request with proper summary
- `/review` - Request code review with quality checks
- `/fix` - Fix bugs and issues systematically
- `/test` - Write and run comprehensive tests
- `/debug` - Debug errors and failures

### Design & Architecture

- `/api` - Design or review API endpoints
- `/db` - Design database schemas and migrations
- `/refactor` - Refactor code for better maintainability

### Documentation & Deployment

- `/docs` - Create or update documentation
- `/deploy` - Deploy application to production
- `/setup` - Set up development environment

### Quality & Security

- `/security` - Security audit and vulnerability check
- `/optimize` - Performance optimization
- `/clean` - Code cleanup and formatting

Run `/help` in your CLI to see all available commands with descriptions.

## 📚 Available Agents

### Planning & Requirements

#### `@research`

Conducts technical research for development decisions, library comparisons, and
architectural guidance.

**Use when:**

- Comparing libraries or frameworks
- Researching best practices
- Making architecture decisions
- Investigating integration patterns

**Example:**

```
@research Compare React state management options for a large enterprise app
```

#### `@prd`

Creates comprehensive Product Requirements Documents with user stories and
technical specifications.

**Use when:**

- Starting a new feature
- Documenting requirements
- Planning feature implementation

**Example:**

```
@prd Create a PRD for user authentication with OAuth and magic links
```

---

### Development & Implementation

#### `@component-implementation`

Creates UI components with accessibility, responsive design, and best practices.

**Use when:**

- Building new UI components
- Implementing frontend features
- Creating reusable component libraries

**Example:**

```
@component-implementation Create a data table component with sorting and filtering
```

#### `@feature-implementation`

Implements business logic, data services, API integration, and state management.

**Use when:**

- Building backend services
- Implementing business logic
- Creating API integrations

**Example:**

```
@feature-implementation Implement user subscription management with Stripe
```

#### `@api-design`

Designs RESTful and GraphQL APIs with authentication, validation, and
documentation.

**Use when:**

- Creating new API endpoints
- Designing API architecture
- Documenting APIs

**Example:**

```
@api-design Design a REST API for a blog platform with posts, comments, and tags
```

#### `@database-design`

Designs database schemas, optimizes queries, and handles migrations.

**Use when:**

- Creating database schemas
- Optimizing queries
- Planning data models

**Example:**

```
@database-design Design a schema for a multi-tenant SaaS application
```

---

### Infrastructure & Tooling

#### `@infrastructure`

Sets up build systems, TypeScript, testing frameworks, and development
environment.

**Use when:**

- Setting up new projects
- Configuring build tools
- Adding TypeScript or testing

**Example:**

```
@infrastructure Set up Vite with React, TypeScript, and Vitest for testing
```

#### `@devops`

Handles deployment, CI/CD, cloud infrastructure, and monitoring.

**Use when:**

- Setting up deployment pipelines
- Configuring cloud infrastructure
- Implementing monitoring

**Example:**

```
@devops Set up GitHub Actions CI/CD with deployment to AWS
```

---

### Quality & Maintenance

#### `@testing`

Creates comprehensive test suites including unit, integration, and E2E tests.

**Use when:**

- Writing tests for new features
- Improving test coverage
- Setting up testing infrastructure

**Example:**

```
@testing Write tests for the user authentication service
```

#### `@quality`

Reviews code quality, validates accessibility, checks security, and assesses
compliance.

**Use when:**

- Performing code reviews
- Validating accessibility
- Checking for security issues

**Example:**

```
@quality Review this PR for security vulnerabilities and accessibility issues
```

#### `@polish`

Optimizes performance, enhances accessibility, improves error handling, and adds
UX polish.

**Use when:**

- Optimizing existing features
- Improving user experience
- Preparing for production

**Example:**

```
@polish Optimize this dashboard for performance and add loading states
```

#### `@code-reviewer`

Reviews code for best practices, potential bugs, and maintainability
(read-only).

**Use when:**

- Getting feedback on code
- Learning best practices
- Planning refactoring

**Example:**

```
@code-reviewer Review this authentication implementation for issues
```

#### `@refactoring`

Improves code structure, removes duplication, and enhances maintainability.

**Use when:**

- Cleaning up technical debt
- Improving code organization
- Simplifying complex code

**Example:**

```
@refactoring Simplify this complex payment processing logic
```

#### `@security-audit`

Performs security audits and identifies vulnerabilities (read-only).

**Use when:**

- Auditing security
- Checking for vulnerabilities
- Preparing for security review

**Example:**

```
@security-audit Audit this API for security vulnerabilities
```

---

### Documentation

#### `@documentation`

Creates technical documentation, API docs, README files, and user guides.

**Use when:**

- Writing documentation
- Creating API documentation
- Updating README files

**Example:**

```
@documentation Create API documentation for our user endpoints
```

---

## 💡 Usage Tips

### Invoking Agents

#### OpenCode

**Direct invocation** with `@` mention:

```
@research What's the best way to handle file uploads in Node.js?
```

**Automatic invocation** by primary agents: Primary agents (build, plan) will
automatically invoke specialized agents when appropriate based on their
descriptions.

#### Claude Code

**Automatic delegation**: Claude Code will automatically delegate tasks to
appropriate agents based on context and the agent's description field.

**Explicit invocation**:

```
> Use the research subagent to investigate file upload libraries
> Ask the testing subagent to write tests for this feature
```

### Using Commands

Both platforms support custom slash commands:

```
/commit              # Review changes and create a commit
/test                # Run tests with coverage
/review              # Review recent changes
/deploy              # Deploy to production
```

Run `/help` to see all available commands.

### Combining Agents

You can chain agent work for complex tasks:

```
1. @research Compare authentication libraries for Node.js
2. @prd Create a PRD for user authentication based on the research
3. @feature-implementation Implement the authentication system
4. @testing Write comprehensive tests for authentication
5. @security-audit Audit the authentication implementation
6. @documentation Document the authentication API
```

### Switching Between Sessions

When subagents create child sessions, navigate with:

- **Ctrl+Right**: Cycle forward through sessions
- **Ctrl+Left**: Cycle backward through sessions

### Customizing Agents and Commands

#### Agent Files

Edit the Markdown file with YAML frontmatter:

```markdown
---
name: my-custom-agent
description: Brief description of when to use this agent
mode: subagent
temperature: 0.2
model: inherit
tools: Read, Write, Edit, Bash
---

Your custom instructions here...
```

#### Command Files

Custom commands support arguments and bash execution:

```markdown
---
description: Brief description of what this command does
allowed-tools: Bash(git:*)
argument-hint: [branch-name]
---

Your command prompt here. Use $ARGUMENTS or $1, $2 for positional arguments.
Execute bash with !`command here`
```

## 🎯 Common Workflows

### Starting a New Feature

```
1. @research Investigate best approaches for [feature]
2. @prd Create PRD for [feature] based on research
3. @database-design Design schema for [feature]
4. @api-design Design API endpoints for [feature]
5. @component-implementation Build UI components
6. @feature-implementation Build backend logic
7. @testing Write comprehensive tests
8. @documentation Create documentation
9. @quality Final quality review
```

### Improving Existing Code

```
1. @code-reviewer Review current implementation
2. @refactoring Refactor based on review feedback
3. @polish Add performance optimizations
4. @testing Ensure test coverage
5. @quality Validate improvements
```

### Security Review

```
1. @security-audit Audit application for vulnerabilities
2. Fix critical issues
3. @quality Validate security fixes
4. @documentation Update security documentation
```

### Setting Up New Project

```
1. @research Compare tech stack options
2. @infrastructure Set up build system and tooling
3. @devops Configure CI/CD pipeline
4. @database-design Design initial schema
5. @api-design Design API architecture
6. @documentation Create project documentation
```

## 🔧 Configuration

### Temperature Settings

Agents use different temperature settings for different types of work:

- **0.1**: Security audits, quality reviews (very focused)
- **0.2**: Implementation, refactoring (balanced)
- **0.3**: Research, documentation (slightly creative)

### Tool Access

Most agents have appropriate tool access:

- **Read-only agents**: code-reviewer, security-audit (no write/edit)
- **Implementation agents**: Full access (write, edit, bash)
- **Research agents**: Read + web access (webfetch)

### Permissions

#### OpenCode

Override permissions in your `opencode.json`:

```json
{
  "agent": {
    "security-audit": {
      "permission": {
        "bash": "ask"
      }
    }
  }
}
```

#### Claude Code

Manage permissions through:

- `/agents` command for managing agent configurations
- `/permissions` command for viewing and updating permissions
- Project-level `.claude/` directory for project-specific configs

## 📖 Learn More

### OpenCode

- [OpenCode Documentation](https://opencode.ai/docs/)
- [Agent Configuration](https://opencode.ai/docs/agents/)
- [Creating Custom Agents](https://opencode.ai/docs/agents/#create-agents)

### Claude Code

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/overview)
- [Subagents Guide](https://docs.claude.com/en/docs/claude-code/sub-agents)
- [Slash Commands Guide](https://docs.claude.com/en/docs/claude-code/slash-commands)

## 🤝 Contributing

Have an agent to share? Submit a PR with:

- Clear description of what the agent does
- Appropriate tool configuration
- Comprehensive instructions with examples
- Real-world use cases

## 📝 License

These agents are provided as examples and templates. Customize them for your
needs!

---

**Happy coding with specialized agents!** 🚀
