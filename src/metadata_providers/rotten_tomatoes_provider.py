import httpx
from typing import Optional, Dict
from src.metadata_providers.base_provider import BaseMetadataProvider

class RottenTomatoesProvider(BaseMetadataProvider):
    """Metadata provider implementation for Rotten Tomatoes."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.rottentomatoes.com/api/public/v1.0/movies.json"

    async def fetch_metadata(self, title: str) -> Optional[Dict]:
        """Fetch metadata for a movie from Rotten Tomatoes."""
        params = {"apikey": self.api_key, "q": title}
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("movies")[0] if data.get("movies") else None
