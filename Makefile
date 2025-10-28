.PHONY: build clean install-opencode install-claude install-all help check-deps

.DEFAULT_GOAL := install-all

help:
	@echo "Available targets:"
	@echo "  install-all        - Install for both OpenCode and Claude Code (default)"
	@echo "  install-opencode   - Install for OpenCode only"
	@echo "  install-claude     - Install for Claude Code only"
	@echo "  build              - Build platform-specific files from source"
	@echo "  clean              - Remove build directory"
	@echo ""
	@echo "Quick start: Just run 'make' to install everything!"

# Check and install dependencies
check-deps:
	@bash scripts/check_deps.sh

# Build platform-specific files
build: check-deps
	@echo "Building platform-specific files..."
	@python3 scripts/build.py

# Clean build directory
clean:
	@rm -rf build/
	@echo "✓ Build directory cleaned"

# OpenCode installation
install-opencode: build
	@echo "Installing for OpenCode..."
	@if [ -d ~/.config/opencode/agent/ ] && [ -n "$$(ls -A ~/.config/opencode/agent/ 2>/dev/null)" ]; then \
		echo "Backing up existing agents to ~/.config/opencode/agent.backup/..."; \
		mkdir -p ~/.config/opencode/agent.backup/; \
		cp -r ~/.config/opencode/agent/* ~/.config/opencode/agent.backup/ 2>/dev/null || true; \
	fi
	@if [ -d ~/.config/opencode/command/ ] && [ -n "$$(ls -A ~/.config/opencode/command/ 2>/dev/null)" ]; then \
		echo "Backing up existing commands to ~/.config/opencode/command.backup/..."; \
		mkdir -p ~/.config/opencode/command.backup/; \
		cp -r ~/.config/opencode/command/* ~/.config/opencode/command.backup/ 2>/dev/null || true; \
	fi
	@mkdir -p ~/.config/opencode/agent/
	@mkdir -p ~/.config/opencode/command/
	@cp build/opencode/agent/*.md ~/.config/opencode/agent/
	@cp build/opencode/command/*.md ~/.config/opencode/command/
	@echo "✓ Agents installed to ~/.config/opencode/agent/"
	@echo "✓ Commands installed to ~/.config/opencode/command/"
	@echo "✓ OpenCode installation complete!"

# Claude Code installation
install-claude: build
	@echo "Installing for Claude Code..."
	@if [ -d ~/.claude/agents/ ] && [ -n "$$(ls -A ~/.claude/agents/ 2>/dev/null)" ]; then \
		echo "Backing up existing agents to ~/.claude/agents.backup/..."; \
		mkdir -p ~/.claude/agents.backup/; \
		cp -r ~/.claude/agents/* ~/.claude/agents.backup/ 2>/dev/null || true; \
	fi
	@if [ -d ~/.claude/commands/ ] && [ -n "$$(ls -A ~/.claude/commands/ 2>/dev/null)" ]; then \
		echo "Backing up existing commands to ~/.claude/commands.backup/..."; \
		mkdir -p ~/.claude/commands.backup/; \
		cp -r ~/.claude/commands/* ~/.claude/commands.backup/ 2>/dev/null || true; \
	fi
	@mkdir -p ~/.claude/agents/
	@mkdir -p ~/.claude/commands/
	@cp build/claude/agents/*.md ~/.claude/agents/
	@cp build/claude/commands/*.md ~/.claude/commands/
	@echo "✓ Agents installed to ~/.claude/agents/"
	@echo "✓ Commands installed to ~/.claude/commands/"
	@echo "✓ Claude Code installation complete!"

# Install for both systems
install-all: install-opencode install-claude
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "✓ Installation complete for both OpenCode and Claude Code!"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo ""
	@echo "📦 Installed:"
	@echo "  • 15 specialized agents (research, testing, security, etc.)"
	@echo "  • 16 custom commands (/commit, /test, /deploy, etc.)"
	@echo ""
	@echo "🚀 Usage:"
	@echo "  OpenCode:     Invoke agents with @agent-name"
	@echo "  Claude Code:  Agents auto-delegate or use explicit requests"
	@echo "  Commands:     Use /command-name on both platforms"
	@echo ""
	@echo "📚 Examples:"
	@echo "  @research Compare state management options"
	@echo "  @testing Write tests for authentication"
	@echo "  /commit"
	@echo "  /review"
	@echo ""
	@echo "Need help? Run: opencode --help  or  claude --help"
	@echo ""
