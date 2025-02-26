# Storage Directory

The `storage` directory implements data persistence and storage management for the OpenHands framework.

## Core Components

### Conversation Storage
- `conversation_store.py`: Base conversation storage interface
- `file_conversation_store.py`: File-based conversation storage
- Handles persistent storage of conversations and related data

### File Storage
- `file_store.py`: File system operations
- `file_utils.py`: File handling utilities
- Manages file operations and persistence

### Settings Storage
- `settings_store.py`: Application settings storage
- `settings_utils.py`: Settings management utilities
- Handles configuration persistence

### Storage Types
- Local file system storage
- Memory-based storage
- Database storage options
- Cloud storage integration

## Key Features
- Multiple storage backends
- Atomic operations
- Data integrity checks
- Concurrent access support
- Backup and recovery

## Implementation Details

### Conversation Storage
- Thread-safe operations
- Versioning support
- Search capabilities
- Compression options
- Cleanup utilities

### File Operations
- Safe file handling
- Path management
- Permission handling
- Temporary file support
- File locking

### Settings Management
- Configuration persistence
- Default handling
- Environment integration
- Override management

### Storage Backends
- File system implementation
- Memory cache support
- Database integration
- Cloud storage options

## Usage
The storage system is used for:
1. Conversation persistence
2. File management
3. Settings storage
4. Data backup
5. Resource management

## Integration Points
- Used by memory system
- Connected to controller
- Integrated with security
- Used by agents for data access

## Data Lifecycle
1. Data creation/modification
2. Storage selection
3. Persistence handling
4. Retrieval operations
5. Cleanup and maintenance

## Security Features
- Access control
- Data encryption
- Integrity verification
- Audit logging
- Backup protection