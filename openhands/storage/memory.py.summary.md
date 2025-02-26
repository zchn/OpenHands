# Memory Storage (memory.py)

This module implements in-memory storage functionality for the OpenHands framework, providing fast access to temporary data and caching capabilities.

## Key Features

### Memory Management
- In-memory data storage
- Cache implementation
- Memory limits
- Garbage collection
- Resource tracking

### Storage Operations
- Key-value storage
- Object caching
- Temporary storage
- Data expiration
- Atomic operations

### Performance Features
- Fast access times
- Thread safety
- Memory efficiency
- Resource limits
- Eviction policies

## Implementation Details

### Core Operations
1. Data Storage
   - Set/Get operations
   - Delete operations
   - Clear operations
   - Existence checks
   - Size tracking

2. Cache Management
   - TTL support
   - LRU eviction
   - Size limits
   - Statistics
   - Monitoring

3. Resource Control
   - Memory limits
   - Item counts
   - Usage tracking
   - Cleanup policies
   - Resource alerts

### Integration Points
- Temporary storage backend
- Cache layer
- Session storage
- Quick lookups
- Data buffering

## Usage Patterns

### Basic Operations
```python
store = MemoryStorage()
store.set("key", "value")
value = store.get("key")
store.delete("key")
```

### Cache Operations
```python
cache = MemoryCache(max_size=1000)
cache.set("key", data, ttl=3600)
data = cache.get("key")
```

### Advanced Features
```python
# With automatic expiration
store.set_with_ttl("key", value, ttl=60)

# Atomic operations
store.increment("counter")
store.append("list", item)
```

## Error Handling
- Memory exhaustion
- Key conflicts
- Type errors
- Limit exceeded
- Timeout errors

## Performance Considerations
1. Memory Usage
   - Size monitoring
   - Eviction policies
   - Garbage collection
   - Resource limits

2. Concurrency
   - Thread safety
   - Lock management
   - Atomic operations
   - Race conditions

3. Efficiency
   - Fast lookups
   - Minimal copying
   - Resource pooling
   - Cache hits

## Best Practices
1. Resource Management
   - Set size limits
   - Monitor usage
   - Handle eviction
   - Clean up regularly

2. Error Handling
   - Check memory
   - Validate input
   - Handle timeouts
   - Log operations

3. Performance
   - Use appropriate structures
   - Implement caching
   - Monitor metrics
   - Optimize access

## Configuration Options
```python
config = {
    "max_size": "1GB",
    "max_items": 10000,
    "ttl_default": 3600,
    "eviction_policy": "lru"
}
```

## Monitoring
- Memory usage
- Item counts
- Hit rates
- Eviction rates
- Error rates