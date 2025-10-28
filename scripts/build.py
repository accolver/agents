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
    except:
        return None, content

def tools_dict_to_claude_list(tools_dict):
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
    tools_list = tools_dict_to_claude_list(config.get('tools'))
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
    frontmatter_lines = ['---']
    
    if 'description' in config:
        frontmatter_lines.append(f"description: {config['description']}")
    
    # Check if body has bash commands (!)
    if '!`' in body:
        # Extract bash commands and build allowed-tools
        bash_cmds = re.findall(r'!\`([^`]+)\`', body)
        if bash_cmds:
            # Extract base commands
            base_cmds = set()
            for cmd in bash_cmds:
                parts = cmd.strip().split()
                if parts:
                    base_cmd = parts[0]
                    base_cmds.add(f"Bash({base_cmd}:*)")
            
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
        with open(agent_file, 'r') as f:
            content = f.read()
        
        config, body = parse_opencode_frontmatter(content)
        if config is None:
            print(f"Warning: Could not parse {agent_file}, skipping")
            continue
        
        # Generate OpenCode version
        opencode_content = build_opencode_agent(config, body, agent_file.name)
        opencode_path = Path(opencode_dir) / agent_file.name
        with open(opencode_path, 'w') as f:
            f.write(opencode_content)
        
        # Generate Claude Code version
        claude_content = build_claude_agent(config, body, agent_file.name)
        claude_path = Path(claude_dir) / agent_file.name
        with open(claude_path, 'w') as f:
            f.write(claude_content)
        
        print(f"✓ Built {agent_file.name}")

def process_commands(source_dir, opencode_dir, claude_dir):
    """Process all command files"""
    source_path = Path(source_dir)
    
    for cmd_file in source_path.glob('*.md'):
        if cmd_file.name == 'README.md':
            continue
            
        with open(cmd_file, 'r') as f:
            content = f.read()
        
        config, body = parse_opencode_frontmatter(content)
        if config is None:
            print(f"Warning: Could not parse {cmd_file}, skipping")
            continue
        
        # Generate OpenCode version
        opencode_content = build_opencode_command(config, body, cmd_file.name)
        opencode_path = Path(opencode_dir) / cmd_file.name
        with open(opencode_path, 'w') as f:
            f.write(opencode_content)
        
        # Generate Claude Code version
        claude_content = build_claude_command(config, body, cmd_file.name)
        claude_path = Path(claude_dir) / cmd_file.name
        with open(claude_path, 'w') as f:
            f.write(claude_content)
        
        print(f"✓ Built {cmd_file.name}")

def main():
    base_dir = Path(__file__).parent.parent
    
    # Create build directories
    (base_dir / 'build/opencode/agent').mkdir(parents=True, exist_ok=True)
    (base_dir / 'build/opencode/command').mkdir(parents=True, exist_ok=True)
    (base_dir / 'build/claude/agents').mkdir(parents=True, exist_ok=True)
    (base_dir / 'build/claude/commands').mkdir(parents=True, exist_ok=True)
    
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
