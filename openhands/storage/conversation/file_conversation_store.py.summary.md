# FileConversationStore (file_conversation_store.py)

This file implements a file-based storage system for conversation metadata, implementing the `ConversationStore` abstract class.

## Key Features
- File-based implementation of the ConversationStore interface
- Uses JSON for metadata serialization
- Supports pagination in search operations
- Handles backward compatibility for GitHub user IDs (converts int to str)

## Implementation Details
- Uses a FileStore backend for actual file operations
- Stores conversations in a directory structure defined by CONVERSATION_BASE_DIR
- Implements all required CRUD operations from the base class
- Includes sorting functionality based on conversation creation time

## Notable Methods
- `save_metadata`: Saves conversation metadata as JSON files
- `get_metadata`: Reads and deserializes JSON metadata with type validation
- `delete_metadata`: Removes conversation metadata files
- `search`: Implements paginated search with sorting by creation date
- `get_instance`: Factory method that creates FileConversationStore instances

## Error Handling
- Handles FileNotFoundError for non-existent conversations
- Includes logging for errors during metadata loading
- Validates metadata using Pydantic type adapters