# Agent Hub Directory

The `agenthub` directory contains various specialized agent implementations for different tasks and capabilities.

## Agent Types

### Browsing Agent (`browsing_agent/`)
- Main agent for web browsing interactions
- Includes response parsing and utility functions
- Handles web navigation and content extraction

### CodeAct Agent (`codeact_agent/`)
- Specialized for code-related actions
- Implements function calling capabilities
- Handles code analysis and modifications

### Delegator Agent (`delegator_agent/`)
- Manages task delegation between agents
- Coordinates complex multi-agent operations
- Handles agent selection and task distribution

### Visual Browsing Agent (`visualbrowsing_agent/`)
- Enhanced browsing agent with visual capabilities
- Handles visual element interaction
- Supports screenshot analysis and visual navigation

### Micro Agents (`micro/`)
- Lightweight agent implementation
- Registry for micro-agent management
- Handles simple, focused tasks

### Dummy Agent (`dummy_agent/`)
- Test implementation for agent interface
- Used for development and testing
- Provides basic agent functionality examples

## Key Features
- Modular agent design allowing easy extension
- Specialized agents for specific task types
- Common utilities and shared functionality
- Clear separation of concerns between agent types

## Implementation Details
Each agent type follows a consistent pattern:
- Clear interface definition
- Task-specific implementations
- Utility functions for common operations
- Error handling and logging

## Usage
Agents can be used individually or composed together for complex tasks. The delegator agent can coordinate between different agent types when needed.