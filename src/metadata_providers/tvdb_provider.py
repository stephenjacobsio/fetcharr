import httpx
from typing import Optional, Dict
from src.metadata_providers.base_provider import BaseMetadataProvider

class TVDbProvider(BaseMetadataProvider):
    """Metadata provider implementation for TVDb."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.thetvdb.com/search/series"

    async def fetch_metadata(self, title: str) -> Optional[Dict]:
        """Fetch metadata for a TV show from TVDb."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"name": title}
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("data")[0] if data.get("data") else None