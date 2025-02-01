import httpx
from typing import Optional, Dict
from src.metadata_providers.base_provider import BaseMetadataProvider

class IMDbProvider(BaseMetadataProvider):
    """Metadata provider implementation for IMDb."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.imdb.com/v1/movies/search"

    async def fetch_metadata(self, title: str) -> Optional[Dict]:
        """Fetch metadata for a movie from IMDb."""
        params = {"api_key": self.api_key, "query": title}
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("results")[0] if data.get("results") else None
