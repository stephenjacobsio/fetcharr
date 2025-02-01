from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.analytics_service import AnalyticsService
from src.core.database import get_db

router = APIRouter()

def get_analytics_service(db: AsyncSession = Depends(get_db)):
    return AnalyticsService(db)

@router.get("/top-genres")
async def get_top_genres(
    user_id: str,
    analytics_service: AnalyticsService = Depends(get_analytics_service)
):
    """Fetch the user's most watched genres."""
    try:
        return await analytics_service.get_top_genres(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/top-actors")
async def get_top_actors(
    user_id: str,
    analytics_service: AnalyticsService = Depends(get_analytics_service)
):
    """Fetch the user's most watched actors."""
    try:
        return await analytics_service.get_top_actors(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))