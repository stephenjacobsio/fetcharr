from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.watch_history_service import WatchHistoryService
from src.core.database import get_db

router = APIRouter()

def get_watch_history_service(db: AsyncSession = Depends(get_db)):
    return WatchHistoryService(db)

@router.get("/")
async def get_watch_history(
    user_id: str,
    watch_history_service: WatchHistoryService = Depends(get_watch_history_service)
):
    """Fetch the watch history for a user from multiple sources."""
    try:
        return await watch_history_service.get_user_history(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sync")
async def sync_watch_history(
    user_id: str,
    watch_history_service: WatchHistoryService = Depends(get_watch_history_service)
):
    """Sync watch history from external services like Trakt, Letterboxd, and Jellyfin."""
    try:
        return await watch_history_service.sync_user_history(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))