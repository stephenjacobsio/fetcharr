from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.core.models import WatchHistory

class AnalyticsService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_top_genres(self, user_id: str):
        """Retrieve the most-watched genres for a user."""
        async with self.db as session:
            result = await session.execute(
                select(WatchHistory.genre, func.count(WatchHistory.genre))
                .where(WatchHistory.user_id == user_id)
                .group_by(WatchHistory.genre)
                .order_by(func.count(WatchHistory.genre).desc())
            )
            return result.all()

    async def get_top_actors(self, user_id: str):
        """Retrieve the most-watched actors for a user."""
        async with self.db as session:
            result = await session.execute(
                select(WatchHistory.actor, func.count(WatchHistory.actor))
                .where(WatchHistory.user_id == user_id)
                .group_by(WatchHistory.actor)
                .order_by(func.count(WatchHistory.actor).desc())
            )
            return result.all()