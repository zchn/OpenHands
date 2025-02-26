# Controller Directory

The `controller` directory manages agent execution and task control, serving as the orchestration layer for the OpenHands framework.

## Core Components

### Agent Controller (`agent_controller.py`)
- Main controller for agent execution
- Manages agent lifecycle and state
- Handles task progression and control flow

### Action Parser (`action_parser.py`)
- Parses and validates agent actions
- Converts raw actions to structured formats
- Handles action validation and normalization

### State Management (`state/`)
- `state.py`: Manages agent and task state
- `task.py`: Task definition and management
- Handles state transitions and persistence

### Replay System (`replay.py`)
- Implements action replay capabilities
- Useful for debugging and testing
- Supports step-by-step replay of agent actions

### Stuck Detection (`stuck.py`)
- Detects when agents are stuck or in loops
- Implements recovery strategies
- Monitors agent progress and performance

## Key Features
- Centralized control of agent execution
- Robust state management system
- Action validation and parsing
- Replay capabilities for debugging
- Stuck detection and recovery

## Implementation Details
The controller system:
- Maintains agent state throughout execution
- Validates and processes agent actions
- Handles error conditions and recovery
- Provides debugging and monitoring tools

## Usage
The controller is the central coordination point for agent operations:
1. Initialize controller with agent configuration
2. Submit tasks for execution
3. Monitor and manage task progression
4. Handle completion and error states

## Integration Points
- Works with the event system for action/observation flow
- Integrates with runtime for execution environment
- Connects with memory system for state persistence
- Interfaces with security for action validation