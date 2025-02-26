# LLM (Language Model) Directory

The `llm` directory contains components for interacting with Large Language Models, providing abstractions and utilities for model integration.

## Core Components

### Base Implementations
- `llm.py`: Base LLM interface and implementation
- `async_llm.py`: Asynchronous LLM operations
- `streaming_llm.py`: Streaming response handling
- `bedrock.py`: AWS Bedrock integration

### Function Calling
- `fn_call_converter.py`: Function call parsing and conversion
- Handles structured function calls from LLM responses
- Converts between different function calling formats

### Mixins
- `debug_mixin.py`: Debugging capabilities
- `retry_mixin.py`: Retry logic for failed calls
- Enhances base LLM functionality

### Metrics
- `metrics.py`: Performance and usage metrics
- Tracks token usage, latency, and costs
- Provides monitoring capabilities

## Key Features
- Unified LLM interface
- Async and streaming support
- Function calling capabilities
- Retry and error handling
- Performance monitoring
- Multiple model support

## Implementation Details

### LLM Interface
- Common interface for all models
- Support for different model providers
- Configurable parameters
- Response validation

### Async Operations
- Non-blocking API calls
- Concurrent request handling
- Stream processing
- Resource management

### Function Calling
- Structured output parsing
- Function definition handling
- Type validation
- Error recovery

### Monitoring
- Token counting
- Cost tracking
- Latency monitoring
- Usage statistics

## Usage
The LLM components are used for:
1. Model interaction
2. Function calling
3. Response streaming
4. Error handling
5. Performance monitoring

## Integration Points
- Used by agents for decision making
- Integrated with memory system
- Connected to security for validation
- Used by controller for task processing

## Supported Models
- OpenAI GPT models
- AWS Bedrock models
- Extensible for other providers