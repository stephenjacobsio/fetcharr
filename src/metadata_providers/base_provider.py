from abc import ABC, abstractmethod
from typing import Optional, Dict

class BaseMetadataProvider(ABC):
    """Abstract base class for metadata providers."""

    @abstractmethod
    async def fetch_metadata(self, title: str) -> Optional[Dict]:
        """Fetch metadata for a given title."""
        pass
