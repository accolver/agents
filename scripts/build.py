#!/usr/bin/env python3
"""
Build script to generate platform-specific agent and command files.
Reads from agent/ and command/ directories and generates:
- build/opencode/ - OpenCode-compatible files
- build/claude/ - Claude Code-compatible files
"""

import os
import re
import sys
from pathlib import Path
import yaml

def parse_opencode_frontmatter(content):
    """Parse OpenCode-style YAML frontmatter"""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return None, content

    frontmatter_text, body = match.groups()
    try:
        config = yaml.safe_load(frontmatter_text)
        return config, body
    except yaml.YAMLError as e:
        print(f"Warning: YAML parse error: {e}")
        return None, content
    except Exception as e:
        print(f"Warning: Unexpected error parsing frontmatter: {e}")
        return None, content

def tools_dict_to_claude_list(tools_dict, filename=None):
    """Convert OpenCode tools dict to Claude Code comma-separated list"""
    if not tools_dict:
        return None

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

    # Validate tool names
    invalid_tools = set(tools_dict.keys()) - set(tool_mapping.keys())
    if invalid_tools:
        file_ref = f" in {filename}" if filename else ""
        print(f"Warning: Unknown tools found{file_ref}: {invalid_tools}")
        print(f"  Valid tools are: {set(tool_mapping.keys())}")

    enabled_tools = []
    for key, value in tools_dict.items():
        if value and key in tool_mapping:
            enabled_tools.append(tool_mapping[key])

    return ', '.join(enabled_tools) if enabled_tools else None

def build_opencode_agent(config, body, filename):
    """Generate OpenCode-format agent file"""
    # OpenCode format is already correct, just return as-is
    frontmatter_lines = ['---']
    if 'description' in config:
        frontmatter_lines.append(f"description: {config['description']}")
    if 'mode' in config:
        frontmatter_lines.append(f"mode: {config['mode']}")
    if 'temperature' in config:
        frontmatter_lines.append(f"temperature: {config['temperature']}")
    
    if 'tools' in config and isinstance(config['tools'], dict):
        frontmatter_lines.append('tools:')
        for tool, enabled in config['tools'].items():
            frontmatter_lines.append(f"  {tool}: {str(enabled).lower()}")
    
    frontmatter_lines.append('---')
    
    return '\n'.join(frontmatter_lines) + '\n' + body

def build_claude_agent(config, body, filename):
    """Generate Claude Code-format agent file"""
    name = Path(filename).stem
    
    frontmatter_lines = ['---']
    frontmatter_lines.append(f"name: {name}")
    
    if 'description' in config:
        frontmatter_lines.append(f"description: {config['description']}")
    
    # Claude Code uses comma-separated tools
    tools_list = tools_dict_to_claude_list(config.get('tools'), filename)
    if tools_list:
        frontmatter_lines.append(f"tools: {tools_list}")
    
    # Add model field (Claude Code specific)
    frontmatter_lines.append('model: inherit')
    
    frontmatter_lines.append('---')
    
    return '\n'.join(frontmatter_lines) + '\n' + body

def build_opencode_command(config, body, filename):
    """Generate OpenCode-format command file"""
    # Commands are mostly compatible, just return as-is
    frontmatter_lines = ['---']
    
    for key, value in config.items():
        if key == 'tools' and isinstance(value, dict):
            frontmatter_lines.append('tools:')
            for tool, enabled in value.items():
                frontmatter_lines.append(f"  {tool}: {str(enabled).lower()}")
        else:
            frontmatter_lines.append(f"{key}: {value}")
    
    frontmatter_lines.append('---')
    
    return '\n'.join(frontmatter_lines) + '\n' + body

def build_claude_command(config, body, filename):
    """Generate Claude Code-format command file"""
    # Whitelist of safe base commands
    SAFE_COMMANDS = {
        'git', 'npm', 'npx', 'python', 'python3', 'make', 'ls', 'cat', 'echo',
        'grep', 'find', 'sed', 'awk', 'curl', 'wget', 'node', 'deno',
        'pnpm', 'yarn', 'bun', 'docker', 'kubectl', 'terraform',
        'cd', 'pwd', 'mkdir', 'rm', 'cp', 'mv', 'chmod', 'test'
    }

    frontmatter_lines = ['---']

    if 'description' in config:
        frontmatter_lines.append(f"description: {config['description']}")

    # Check if body has bash commands (!)
    if '!`' in body:
        # Extract bash commands and build allowed-tools
        bash_cmds = re.findall(r'!\`([^`]+)\`', body)
        if bash_cmds:
            # Extract base commands with validation
            base_cmds = set()
            for cmd in bash_cmds:
                parts = cmd.strip().split()
                if parts:
                    base_cmd = parts[0]
                    # Validate against whitelist
                    if base_cmd in SAFE_COMMANDS:
                        base_cmds.add(f"Bash({base_cmd}:*)")
                    else:
                        print(f"Warning: Skipping potentially unsafe command in {filename}: {base_cmd}")

            if base_cmds:
                frontmatter_lines.append(f"allowed-tools: {', '.join(sorted(base_cmds))}")
    
    # Check for argument usage
    if '$ARGUMENTS' in body or re.search(r'\$\d+', body):
        if 'argument-hint' not in config:
            frontmatter_lines.append('argument-hint: [args]')
    
    frontmatter_lines.append('---')
    
    return '\n'.join(frontmatter_lines) + '\n' + body

def process_agents(source_dir, opencode_dir, claude_dir):
    """Process all agent files"""
    source_path = Path(source_dir)

    for agent_file in source_path.glob('*.md'):
        try:
            with open(agent_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except IOError as e:
            print(f"Error: Could not read {agent_file}: {e}")
            continue
        except Exception as e:
            print(f"Error: Unexpected error reading {agent_file}: {e}")
            continue

        config, body = parse_opencode_frontmatter(content)
        if config is None:
            print(f"Error: Invalid YAML frontmatter in {agent_file.name}")
            print("  → Check that frontmatter starts/ends with '---'")
            print("  → Validate YAML syntax at yamllint.com")
            continue

        try:
            # Generate OpenCode version
            opencode_content = build_opencode_agent(config, body, agent_file.name)
            opencode_path = Path(opencode_dir) / agent_file.name
            with open(opencode_path, 'w', encoding='utf-8') as f:
                f.write(opencode_content)

            # Generate Claude Code version
            claude_content = build_claude_agent(config, body, agent_file.name)
            claude_path = Path(claude_dir) / agent_file.name
            with open(claude_path, 'w', encoding='utf-8') as f:
                f.write(claude_content)

            print(f"✓ Built {agent_file.name}")
        except IOError as e:
            print(f"Error: Could not write output files for {agent_file.name}: {e}")
            continue
        except Exception as e:
            print(f"Error: Unexpected error processing {agent_file.name}: {e}")
            continue

def process_commands(source_dir, opencode_dir, claude_dir):
    """Process all command files"""
    source_path = Path(source_dir)

    for cmd_file in source_path.glob('*.md'):
        if cmd_file.name == 'README.md':
            continue

        try:
            with open(cmd_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except IOError as e:
            print(f"Error: Could not read {cmd_file}: {e}")
            continue
        except Exception as e:
            print(f"Error: Unexpected error reading {cmd_file}: {e}")
            continue

        config, body = parse_opencode_frontmatter(content)
        if config is None:
            print(f"Error: Invalid YAML frontmatter in {cmd_file.name}")
            print("  → Check that frontmatter starts/ends with '---'")
            print("  → Validate YAML syntax at yamllint.com")
            continue

        try:
            # Generate OpenCode version
            opencode_content = build_opencode_command(config, body, cmd_file.name)
            opencode_path = Path(opencode_dir) / cmd_file.name
            with open(opencode_path, 'w', encoding='utf-8') as f:
                f.write(opencode_content)

            # Generate Claude Code version
            claude_content = build_claude_command(config, body, cmd_file.name)
            claude_path = Path(claude_dir) / cmd_file.name
            with open(claude_path, 'w', encoding='utf-8') as f:
                f.write(claude_content)

            print(f"✓ Built {cmd_file.name}")
        except IOError as e:
            print(f"Error: Could not write output files for {cmd_file.name}: {e}")
            continue
        except Exception as e:
            print(f"Error: Unexpected error processing {cmd_file.name}: {e}")
            continue

def ensure_directory(path):
    """Thread-safe directory creation with proper error handling"""
    try:
        path.mkdir(parents=True, exist_ok=True)
        return True
    except OSError as e:
        print(f"Error: Could not create directory {path}: {e}")
        return False
    except Exception as e:
        print(f"Error: Unexpected error creating directory {path}: {e}")
        return False

def main():
    base_dir = Path(__file__).parent.parent

    # Create build directories with error handling
    print("Creating build directories...")
    directories = [
        base_dir / 'build/opencode/agent',
        base_dir / 'build/opencode/command',
        base_dir / 'build/claude/agents',
        base_dir / 'build/claude/commands'
    ]

    for directory in directories:
        if not ensure_directory(directory):
            print(f"Error: Failed to create required directory: {directory}")
            sys.exit(1)

    print("Building agents...")
    process_agents(
        base_dir / 'agent',
        base_dir / 'build/opencode/agent',
        base_dir / 'build/claude/agents'
    )

    print("\nBuilding commands...")
    process_commands(
        base_dir / 'command',
        base_dir / 'build/opencode/command',
        base_dir / 'build/claude/commands'
    )
    
    print("\n✓ Build complete!")
    print(f"  OpenCode files: {base_dir}/build/opencode/")
    print(f"  Claude Code files: {base_dir}/build/claude/")

if __name__ == '__main__':
    main()
