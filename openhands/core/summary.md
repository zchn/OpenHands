# Core Directory

The `core` directory contains the fundamental components and infrastructure of the OpenHands framework.

## Key Components

### Configuration (`config/`)
- `app_config.py`: Main application configuration
- `agent_config.py`: Agent-specific settings
- `llm_config.py`: Language model configuration
- `sandbox_config.py`: Sandbox environment settings
- `security_config.py`: Security policy configuration
- `extended_config.py`: Extended configuration options
- Configuration utilities and helpers

### Schema (`schema/`)
- `action.py`: Action data structures
- `agent.py`: Agent interface definitions
- `observation.py`: Observation data models
- Type definitions and validation

### Main Components
- `main.py`: Application entry point
- `loop.py`: Main event loop implementation
- `cli.py`: Command-line interface
- `setup.py`: Framework initialization

### Messaging System
- `message.py`: Message data structures
- `message_utils.py`: Message handling utilities
- Event and message routing

### Utilities
- `logger.py`: Logging infrastructure
- `download.py`: Resource downloading
- `exceptions.py`: Framework exceptions

## Key Features
- Centralized configuration management
- Type-safe schema definitions
- Robust logging system
- Exception handling framework
- Resource management

## Implementation Details

### Configuration System
- Hierarchical configuration structure
- Environment-aware settings
- Validation and type checking
- Extension points for custom config

### Schema System
- Strong type definitions
- Validation rules
- Serialization support
- Extensible data models

### Event Loop
- Asynchronous operation support
- Event handling and routing
- Resource management
- Error handling and recovery

## Usage
The core components provide the foundation for:
1. Application configuration
2. Type safety and validation
3. Event handling and messaging
4. Resource management
5. Logging and monitoring

## Integration Points
- Used by all other framework components
- Provides base classes and interfaces
- Manages framework lifecycle
- Handles cross-cutting concerns