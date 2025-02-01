from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.jellyfin_service import JellyfinService
from src.core.database import get_db
from src.infrastructure.cache import Cache
from src.config import Settings

router = APIRouter()

# Initialize caching and service
settings = Settings()
cache = Cache(settings.REDIS_URL)

def get_jellyfin_service(db: AsyncSession = Depends(get_db)):
    return JellyfinService(db, cache)

@router.get("/library")
async def get_jellyfin_library(
    api_token: str,
    jellyfin_service: JellyfinService = Depends(get_jellyfin_service)
):
    """Fetch media library from Jellyfin."""
    try:
        return await jellyfin_service.fetch_library(api_token)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))