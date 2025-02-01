import redis.asyncio as redis
import json
from typing import Optional

class RedisCache:
    def __init__(self, redis_url: str):
        """Initialize the Redis connection."""
        self.redis_url = redis_url
        self.client = redis.from_url(self.redis_url, decode_responses=True)

    async def get(self, key: str) -> Optional[dict]:
        """Retrieve a value from Redis by key."""
        value = await self.client.get(key)
        return json.loads(value) if value else None

    async def set(self, key: str, value: dict, ttl: int = 3600):
        """Set a value in Redis with an optional TTL (default: 1 hour)."""
        await self.client.setex(key, ttl, json.dumps(value))

    async def delete(self, key: str):
        """Delete a key from Redis."""
        await self.client.delete(key)

    async def flush(self):
        """Flush all keys from Redis."""
        await self.client.flushdb()

    async def exists(self, key: str) -> bool:
        """Check if a key exists in Redis."""
        return await self.client.exists(key) > 0

    async def keys(self, pattern: str = "*") -> list:
        """Retrieve all keys matching a pattern."""
        return await self.client.keys(pattern)
