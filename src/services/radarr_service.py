import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.cache import Cache


class RadarrService:
    def __init__(self, db: AsyncSession, cache: Cache):
        self.db = db
        self.cache = cache

    async def fetch_movies(self, api_key: str, radarr_url: str):
        """Fetch movie library from Radarr and cache results."""
        cache_key = "radarr_movies"
        cached_data = await self.cache.get(cache_key)

        if cached_data:
            return cached_data

        url = f"{radarr_url}/api/v3/movie"
        params = {"apikey": api_key}

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            await self.cache.set(cache_key, data, ttl=3600)
            return data
