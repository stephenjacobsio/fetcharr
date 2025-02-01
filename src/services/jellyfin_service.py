import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.cache import Cache


class JellyfinService:
    def __init__(self, db: AsyncSession, cache: Cache):
        self.db = db
        self.cache = cache

    async def fetch_library(self, api_token: str):
        """Fetch media library from Jellyfin and cache results."""
        cache_key = f"jellyfin_library_{api_token}"
        cached_data = await self.cache.get(cache_key)

        if cached_data:
            return cached_data

        url = "https://jellyfin.example.com/Users/{user_id}/Items"
        headers = {"Authorization": f"Bearer {api_token}"}

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            await self.cache.set(cache_key, data, ttl=3600)
            return data