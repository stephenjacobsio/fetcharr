from .jellyfin import router as jellyfin_router
from .radarr import router as radarr_router
from .sonarr import router as sonarr_router
from .metadata import router as metadata_router
from .enrich import router as enrich_router

__all__ = [
    "jellyfin_router",
    "radarr_router",
    "sonarr_router",
    "metadata_router",
    "enrich_router",
]