.PHONY: copy-commands copy-agents copy-all

copy-commands:
	@mkdir -p ~/.config/opencode/command/
	@cp command/*.md ~/.config/opencode/command/
	@echo "Commands copied to ~/.config/opencode/command/"

copy-agents:
	@mkdir -p ~/.config/opencode/agent/
	@cp agent/*.md ~/.config/opencode/agent/
	@echo "Agents copied to ~/.config/opencode/agent/"

copy-all: copy-commands copy-agents
	@echo "All agents and commands copied successfully!"
