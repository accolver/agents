# OpenCode Commands Collection

A comprehensive collection of useful custom commands for common development tasks. These commands work with [OpenCode](https://opencode.ai) to streamline your workflow.

## 📋 Overview

Custom commands let you create shortcuts for repetitive tasks. Each command can:

- Run shell commands and capture output
- Reference files in your project
- Accept arguments
- Invoke specific agents
- Use different models

## 🚀 Installation

### Quick Start (Recommended)

Install all commands globally:

```bash
# If you cloned the agents repository
cd agents

# Create the OpenCode command directory (if it doesn't exist)
mkdir -p ~/.config/opencode/command/

# Copy all commands to your global OpenCode config
cp command/*.md ~/.config/opencode/command/

# Verify installation
ls ~/.config/opencode/command/
```

### Per-Project Installation

Install commands for specific projects:

```bash
# In your project directory
mkdir -p .opencode/command/

# Copy all commands or select individual ones
cp /path/to/agents/command/*.md .opencode/command/

# Or copy just specific commands
cp /path/to/agents/command/test.md .opencode/command/
cp /path/to/agents/command/review.md .opencode/command/
```

### Installing Individual Commands

```bash
mkdir -p ~/.config/opencode/command/

# Download a specific command
curl -o ~/.config/opencode/command/test.md \
  https://raw.githubusercontent.com/accolver/agents/main/command/test.md
```

## 📚 Available Commands

### Testing & Quality

#### `/test`

Run tests with coverage and get suggestions for improvements.

**Usage:**

```
/test
```

**What it does:**

- Runs test suite with coverage
- Analyzes pass/fail results
- Identifies low coverage areas
- Suggests specific tests to add

---

#### `/review`

Review recent git changes for quality and best practices.

**Usage:**

```
/review
```

**What it does:**

- Analyzes recent git diff
- Reviews code quality and style
- Identifies potential bugs
- Checks for security issues
- Provides constructive feedback

---

#### `/fix`

Fix linting and TypeScript errors automatically.

**Usage:**

```
/fix
```

**What it does:**

- Runs linter and type checker
- Identifies all errors
- Fixes errors systematically
- Verifies fixes work

---

#### `/security`

Run security audit on dependencies and code.

**Usage:**

```
/security
```

**What it does:**

- Checks for vulnerable dependencies
- Scans for common security issues
- Prioritizes by severity
- Provides remediation steps

---

### Build & Deploy

#### `/build`

Build project and fix any build errors.

**Usage:**

```
/build
```

**What it does:**

- Runs build command
- Identifies build errors
- Fixes errors systematically
- Reports bundle size
- Suggests optimizations

---

#### `/deploy`

Set up or troubleshoot deployment.

**Usage:**

```
/deploy
```

**What it does:**

- Reviews deployment configuration
- Sets up CI/CD pipeline
- Configures deployment platform
- Troubleshoots deployment issues

---

### Code Quality

#### `/optimize`

Optimize performance and bundle size.

**Usage:**

```
/optimize
```

**What it does:**

- Analyzes bundle size
- Identifies optimization opportunities
- Implements code splitting
- Optimizes images and dependencies
- Improves database queries

---

#### `/refactor`

Refactor code for better maintainability.

**Usage:**

```
/refactor src/components/Button.tsx
```

**What it does:**

- Analyzes code smells
- Improves naming and structure
- Removes duplication
- Simplifies complex logic
- Maintains same behavior

---

#### `/clean`

Clean up technical debt and remove dead code.

**Usage:**

```
/clean
```

**What it does:**

- Removes unused code
- Eliminates console.logs
- Cleans commented code
- Addresses TODOs
- Removes unused dependencies

---

### Development Setup

#### `/setup`

Set up complete development environment.

**Usage:**

```
/setup
```

**What it does:**

- Configures TypeScript
- Sets up linting and formatting
- Adds testing framework
- Configures git hooks
- Creates useful npm scripts

---

### Documentation & Git

#### `/docs`

Generate or update project documentation.

**Usage:**

```
/docs
```

**What it does:**

- Updates README.md
- Documents installation and usage
- Lists available scripts
- Adds troubleshooting info
- Creates contribution guidelines

---

#### `/commit`

Review changes and create a meaningful commit.

**Usage:**

```
/commit
```

**What it does:**

- Reviews staged changes
- Suggests commit message
- Follows conventional commits
- Asks for confirmation
- Creates the commit

---

#### `/pr`

Prepare for pull request with quality checks.

**Usage:**

```
/pr
```

**What it does:**

- Summarizes branch changes
- Reviews code quality
- Runs tests and linting
- Generates PR description
- Lists breaking changes

---

### Design & Architecture

#### `/api`

Design or implement an API endpoint.

**Usage:**

```
/api user authentication endpoints
```

**What it does:**

- Designs RESTful endpoints
- Defines request/response schemas
- Adds validation rules
- Provides example code
- Creates API documentation

---

#### `/db`

Design database schema or optimize queries.

**Usage:**

```
/db user and posts relationship
```

**What it does:**

- Designs database schema
- Creates table definitions
- Adds proper indexes
- Defines relationships
- Provides migration scripts

---

### Debugging

#### `/debug`

Debug an issue or error with assistance.

**Usage:**

```
/debug Authentication not working in production
```

**What it does:**

- Clarifies the problem
- Analyzes error messages
- Investigates potential causes
- Provides specific solutions
- Verifies fix works

---

## 💡 Usage Tips

### Basic Usage

Type `/` in the OpenCode TUI to see available commands:

```
/test
/review
/fix
```

### With Arguments

Some commands accept arguments using `$ARGUMENTS`:

```
/refactor src/utils/helpers.ts
/api user profile endpoints
/debug Login button not responding
```

### Command Features

**Shell Output**: Commands can run shell commands and use their output

```markdown
!`npm test`
```

**File References**: Include files in prompts

```markdown
Review @src/components/Button.tsx
```

**Agent Selection**: Commands invoke specialized agents

```yaml
agent: testing
agent: code-reviewer
```

**Subtasks**: Create separate sessions for isolated work

```yaml
subtask: true
```

## 🔧 Customization

### Creating Your Own Commands

Create a markdown file in `~/.config/opencode/command/`:

```markdown
---
description: Your command description
agent: build
model: anthropic/claude-3-5-sonnet-20241022
---

Your command prompt here.
Use $ARGUMENTS for user input.
Use !`shell command` for shell output.
Use @filename for file references.
```

### Modifying Existing Commands

Edit any command file to customize:

- Change the prompt template
- Switch the agent
- Modify shell commands
- Add/remove checks

### Command Examples

**Simple command:**

```markdown
---
description: List all TODO comments
---

Find all TODO comments in the codebase:
!`grep -r "TODO" --include="*.ts" --include="*.js" .`

Create a prioritized list of tasks.
```

**With arguments:**

```markdown
---
description: Create a new component
agent: component-implementation
---

Create a new React component called $ARGUMENTS with:
- TypeScript types
- Props interface
- Proper styling
- Basic tests
```

**With file reference:**

```markdown
---
description: Explain code
---

Explain the code in @$ARGUMENTS
Include:
- What it does
- How it works
- Why it's structured this way
```

## 🎯 Common Workflows

### Before Committing

```
/test        # Ensure tests pass
/fix         # Fix any lint errors
/review      # Review changes
/commit      # Create commit
```

### Code Quality Review

```
/review      # Review recent changes
/security    # Check security
/optimize    # Find performance issues
/clean       # Remove technical debt
```

### Preparing for PR

```
/test        # Run tests
/fix         # Fix errors
/docs        # Update documentation
/pr          # Generate PR description
```

### New Feature Development

```
/api         # Design API endpoints
/db          # Design database schema
/test        # Write tests
/security    # Security review
```

### Debugging Session

```
/debug [issue]     # Debug specific issue
/test              # Verify fix
/review            # Review changes
```

## 📖 Learn More

- [OpenCode Documentation](https://opencode.ai/docs/)
- [Commands Documentation](https://opencode.ai/docs/commands/)
- [Custom Commands Guide](https://opencode.ai/docs/commands/#create-command-files)

## 🤝 Contributing

Have a useful command to share? Submit a PR with:

- Clear description
- Appropriate agent selection
- Useful shell commands
- Example usage

## 📝 License

These commands are provided under the MIT License. Customize them for your needs!

---

**Streamline your workflow with custom commands!** ⚡
