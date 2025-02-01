from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from src.services.filtering_service import FilteringService
from src.core.database import get_db

router = APIRouter()

def get_filtering_service(db: AsyncSession = Depends(get_db)):
    return FilteringService(db)

@router.get("/")
async def filter_media(
    resolution: Optional[str] = None,
    codec: Optional[str] = None,
    audio: Optional[str] = None,
    filtering_service: FilteringService = Depends(get_filtering_service)
):
    """Filter media based on resolution, codec, and audio format."""
    try:
        return await filtering_service.apply_filters(resolution, codec, audio)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
