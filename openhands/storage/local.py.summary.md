# Local Storage (local.py)

This module implements local file system storage functionality for the OpenHands framework, providing a simple and efficient way to store files on the local machine.

## Key Features

### Local Storage Operations
- Direct file system access
- Path management
- Directory operations
- File permissions
- Symbolic links

### Storage Management
- Space monitoring
- Cleanup operations
- Temporary storage
- Cache management
- File organization

### Performance Features
- Direct I/O operations
- Memory mapping
- Buffer management
- File locking
- Atomic operations

## Implementation Details

### Core Operations
1. File Operations
   - Read/Write
   - Copy/Move
   - Delete/Rename
   - Permissions
   - Attributes

2. Directory Operations
   - Creation
   - Deletion
   - Listing
   - Traversal
   - Permissions

3. Path Management
   - Resolution
   - Normalization
   - Validation
   - Security checks
   - Relative paths

### Integration Points
- Base for FileStore
- Supports ConversationStore
- Temporary storage
- Cache backend

## Usage Patterns

### Basic Operations
```python
store = LocalStorage(root_dir="/path/to/storage")
store.write_file("file.txt", content)
content = store.read_file("file.txt")
```

### Directory Management
```python
store.create_directory("new_dir")
files = store.list_directory("path")
store.remove_directory("old_dir")
```

## Error Handling
- Permission errors
- Disk space issues
- File locks
- Path validation
- I/O errors

## Security Features
- Path sanitization
- Permission checks
- Symbolic link handling
- Resource limits
- Access control

## Performance Optimization
1. Caching
   - File handles
   - Directory listings
   - Metadata
   - Path resolution

2. I/O Operations
   - Buffered I/O
   - Direct I/O
   - Memory mapping
   - Asynchronous I/O

3. Resource Management
   - File descriptors
   - Memory usage
   - Disk space
   - Open handles

## Best Practices
1. File Operations
   - Use atomic operations
   - Implement proper locking
   - Handle cleanup
   - Validate paths

2. Error Management
   - Handle disk full
   - Check permissions
   - Validate input
   - Log operations

3. Resource Usage
   - Monitor space
   - Limit file sizes
   - Control concurrency
   - Manage handles