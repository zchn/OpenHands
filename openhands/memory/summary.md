# Memory Directory

The `memory` directory implements memory management and conversation history handling for the OpenHands framework.

## Core Components

### Condenser System (`condenser/`)
Base implementation and interface:
- `condenser.py`: Base condenser interface
- `__init__.py`: Condenser registration and utilities

#### Condenser Implementations (`condenser/impl/`)
- `amortized_forgetting_condenser.py`: Gradual memory decay
- `llm_attention_condenser.py`: Attention-based memory management
- `llm_summarizing_condenser.py`: Summary-based memory compression
- `no_op_condenser.py`: Pass-through implementation
- `observation_masking_condenser.py`: Selective observation storage
- `recent_events_condenser.py`: Recent history management

### Long-term Memory
- `long_term_memory.py`: Persistent memory storage
- Handles long-term information retention
- Manages memory retrieval and storage

## Key Features
- Multiple memory management strategies
- Configurable memory retention
- Memory compression techniques
- Long-term storage support
- Memory search and retrieval

## Implementation Details

### Memory Management Strategies

#### Amortized Forgetting
- Gradual decay of old memories
- Importance-based retention
- Memory cleanup

#### Attention-based
- LLM-guided memory focus
- Context-aware retention
- Dynamic memory prioritization

#### Summarization
- Memory compression through summarization
- Key information extraction
- Context preservation

#### Observation Masking
- Selective memory storage
- Pattern-based filtering
- Memory optimization

### Long-term Memory
- Persistent storage
- Indexing and retrieval
- Memory search
- Context management

## Usage
The memory system is used for:
1. Conversation history management
2. Context preservation
3. Memory optimization
4. Information retrieval
5. Long-term storage

## Integration Points
- Used by agents for context
- Connected to LLM for processing
- Integrated with storage system
- Used by controller for state management

## Memory Lifecycle
1. Event/observation capture
2. Memory processing (condensing)
3. Storage optimization
4. Retrieval on demand
5. Gradual decay or archival