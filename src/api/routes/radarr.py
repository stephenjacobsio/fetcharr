from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.radarr_service import RadarrService
from src.core.database import get_db
from src.infrastructure.cache import Cache
from src.config import Settings

router = APIRouter()

# Initialize caching and service
settings = Settings()
cache = Cache(settings.REDIS_URL)

def get_radarr_service(db: AsyncSession = Depends(get_db)):
    return RadarrService(db, cache)

@router.get("/movies")
async def get_radarr_movies(
    api_key: str,
    radarr_service: RadarrService = Depends(get_radarr_service)
):
    """Fetch movie library from Radarr."""
    try:
        return await radarr_service.fetch_movies(api_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))