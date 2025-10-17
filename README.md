# OpenCode Agents Collection

A comprehensive collection of specialized AI agents for the complete software development lifecycle. These agents work with [OpenCode](https://opencode.ai) to provide focused assistance across all phases of development.

## 📋 Overview

These agents are designed to be **reusable across any project** and cover everything from initial research and planning through to deployment and maintenance. Each agent is a specialized subagent that can be invoked by mentioning it with `@agent-name` or automatically by primary agents when needed.

## 🚀 Installation

### Quick Start (Recommended)

Install all agents globally so they're available in every project:

```bash
# Clone the repository
git clone https://github.com/accolver/agent.git

# Create the OpenCode agent directory (if it doesn't exist)
mkdir -p ~/.config/opencode/agent/

# Copy all agents to your global OpenCode config
cp agent/*.md ~/.config/opencode/agent/

# Verify installation
ls ~/.config/opencode/agent/
```

That's it! The agents are now available in any OpenCode session. Invoke them with `@agent-name`.

### Alternative: Per-Project Installation

If you prefer to install agents only for specific projects:

```bash
# Clone the repository
git clone https://github.com/accolver/agent.git

# In your project directory
cd your-project

# Create project agent directory
mkdir -p .opencode/agent/

# Copy all agents or select individual ones
cp agent/*.md .opencode/agent/

# Or copy just specific agents you need
cp agent/research.md .opencode/agent/
cp agent/testing.md .opencode/agent/
```

### Installing Individual Agents

You can also download and install individual agents:

```bash
# Create agent directory
mkdir -p ~/.config/opencode/agent/

# Download a specific agent (example: research.md)
curl -o ~/.config/opencode/agent/research.md \
  https://raw.githubusercontent.com/accolver/agent/main/research.md
```

### Updating Agents

To update to the latest version:

```bash
# Navigate to the cloned repository
cd agent

# Pull latest changes
git pull

# Copy updated agents
cp *.md ~/.config/opencode/agent/
```

## 📚 Available Agents

### Planning & Requirements

#### `@research`

Conducts technical research for development decisions, library comparisons, and architectural guidance.

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

Creates comprehensive Product Requirements Documents with user stories and technical specifications.

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

Designs RESTful and GraphQL APIs with authentication, validation, and documentation.

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

Sets up build systems, TypeScript, testing frameworks, and development environment.

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

Reviews code quality, validates accessibility, checks security, and assesses compliance.

**Use when:**

- Performing code reviews
- Validating accessibility
- Checking for security issues

**Example:**

```
@quality Review this PR for security vulnerabilities and accessibility issues
```

#### `@polish`

Optimizes performance, enhances accessibility, improves error handling, and adds UX polish.

**Use when:**

- Optimizing existing features
- Improving user experience
- Preparing for production

**Example:**

```
@polish Optimize this dashboard for performance and add loading states
```

#### `@code-reviewer`

Reviews code for best practices, potential bugs, and maintainability (read-only).

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

**Direct invocation** with `@` mention:

```
@research What's the best way to handle file uploads in Node.js?
```

**Automatic invocation** by primary agents:
Primary agents (build, plan) will automatically invoke specialized agents when appropriate based on their descriptions.

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

### Customizing Agents

Each agent can be customized by editing its markdown file:

```markdown
---
description: Your custom description
mode: subagent
temperature: 0.2
tools:
  write: true
  edit: true
---

Your custom instructions here...
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

You can override permissions in your `opencode.json`:

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

## 📖 Learn More

- [OpenCode Documentation](https://opencode.ai/docs/)
- [Agent Configuration](https://opencode.ai/docs/agents/)
- [Creating Custom Agents](https://opencode.ai/docs/agents/#create-agents)

## 🤝 Contributing

Have an agent to share? Submit a PR with:

- Clear description of what the agent does
- Appropriate tool configuration
- Comprehensive instructions with examples
- Real-world use cases

## 📝 License

These agents are provided as examples and templates. Customize them for your needs!

---

**Happy coding with specialized agents!** 🚀
