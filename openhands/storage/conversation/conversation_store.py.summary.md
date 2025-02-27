# ConversationStore (conversation_store.py)

This file defines an abstract base class `ConversationStore` that serves as an interface for storing and managing conversation metadata. 

## Key Features
- Abstract class that defines the contract for conversation storage implementations
- Supports operations for both single and multi-user environments
- Provides methods for CRUD operations on conversation metadata

## Core Methods
- `save_metadata`: Store conversation metadata
- `get_metadata`: Load conversation metadata by ID
- `delete_metadata`: Remove conversation metadata
- `exists`: Check if a conversation exists
- `search`: Search conversations with pagination support
- `get_instance`: Factory method to create store instances

## Usage
This abstract class should be implemented by concrete storage classes that provide specific storage mechanisms (e.g., file-based, database-based).