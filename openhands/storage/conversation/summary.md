# Conversation Storage Directory

This directory contains the implementation of conversation metadata storage for the OpenHands system.

## Files Overview

### conversation_store.py
Defines the abstract interface for conversation storage operations through the `ConversationStore` class. This serves as the contract that all conversation storage implementations must follow.

### file_conversation_store.py
Provides a concrete file-based implementation of the `ConversationStore` interface, storing conversation metadata as JSON files in a structured directory hierarchy.

## Architecture
- Uses an abstract base class pattern to allow for different storage implementations
- Currently implements a file-based storage system
- Supports metadata operations (CRUD) with pagination
- Designed to work in both single-user and multi-user environments

## Key Features
- Abstract interface for storage operations
- File-based implementation with JSON serialization
- Pagination support for conversation listing
- Sorting by conversation creation time
- Error handling and logging
- Type validation using Pydantic

## Usage
The storage system is used to persist conversation metadata, allowing conversations to be saved, retrieved, and searched. The file-based implementation is suitable for development and small-scale deployments, while the abstract interface allows for other implementations (e.g., database-based) to be added as needed.