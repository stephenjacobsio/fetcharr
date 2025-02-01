from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.sonarr_service import SonarrService
from src.core.database import get_db
from src.infrastructure.cache import Cache
from src.config import Settings

router = APIRouter()

# Initialize caching and service
settings = Settings()
cache = Cache(settings.REDIS_URL)

def get_sonarr_service(db: AsyncSession = Depends(get_db)):
    return SonarrService(db, cache)

@router.get("/series")
async def get_sonarr_series(
    api_key: str,
    sonarr_service: SonarrService = Depends(get_sonarr_service)
):
    """Fetch TV series library from Sonarr."""
    try:
        return await sonarr_service.fetch_series(api_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
