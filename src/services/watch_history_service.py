from sqlalchemy import Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.core.models import WatchHistory
from typing import List, Any, Coroutine, Sequence


class WatchHistoryService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_history(self, user_id: str) -> Sequence[Row[Any] | RowMapping | Any]:
        """Fetch watch history for a given user."""
        async with self.db as session:
            result = await session.execute(
                select(WatchHistory).where(user_id == WatchHistory.user_id)
            )
            return result.scalars().all()

    async def sync_user_history(self, user_id: str):
        """Sync watch history from external sources like Trakt, Letterboxd, and Jellyfin."""
        # Placeholder for integrating external APIs
        return {"message": "Watch history sync not implemented yet"}
