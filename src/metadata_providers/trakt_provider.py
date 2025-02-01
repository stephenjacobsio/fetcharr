import httpx
from typing import Optional, Dict
from src.metadata_providers.base_provider import BaseMetadataProvider

class TraktProvider(BaseMetadataProvider):
    """Metadata provider implementation for Trakt."""

    def __init__(self, client_id: str):
        self.client_id = client_id
        self.base_url = "https://api.trakt.tv/search/movie"

    async def fetch_metadata(self, title: str) -> Optional[Dict]:
        """Fetch metadata for a movie from Trakt."""
        headers = {"Content-Type": "application/json", "trakt-api-version": "2", "trakt-api-key": self.client_id}
        params = {"query": title}
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data[0] if data else None
