from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.cache import Cache
from src.metadata_providers.tmdb_provider import TMDbProvider
from src.metadata_providers.imdb_provider import IMDbProvider
from src.metadata_providers.tvdb_provider import TVDbProvider


class MetadataService:
    def __init__(self, db: AsyncSession, cache: Cache):
        self.db = db
        self.cache = cache
        self.providers = [TMDbProvider(), IMDbProvider(), TVDbProvider()]

    async def fetch_metadata(self, title: str):
        """Fetch metadata from multiple providers and return the best match."""
        cache_key = f"metadata_{title}"
        cached_data = await self.cache.get(cache_key)

        if cached_data:
            return cached_data

        results = []
        for provider in self.providers:
            metadata = await provider.fetch_metadata(title)
            if metadata:
                results.append(metadata)

        if results:
            best_match = sorted(results, key=lambda x: x.get("popularity", 0), reverse=True)[0]
            await self.cache.set(cache_key, best_match, ttl=86400)
            return best_match

        return {"error": "No metadata found"}

    async def enrich_metadata(self, title: str):
        """Enhance existing metadata by fetching additional details."""
        metadata = await self.fetch_metadata(title)
        if "error" not in metadata:
            metadata["enriched"] = True
        return metadata
