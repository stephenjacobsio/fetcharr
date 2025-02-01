from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional
from src.core.models import Media


class FilteringService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def apply_filters(
            self,
            resolution: Optional[str] = None,
            codec: Optional[str] = None,
            audio: Optional[str] = None
    ):
        """Filter media based on resolution, codec, and audio format."""
        async with self.db as session:
            query = select(Media)

            if resolution:
                query = query.where(Media.resolution == resolution)
            if codec:
                query = query.where(Media.codec == codec)
            if audio:
                query = query.where(Media.audio_format == audio)

            result = await session.execute(query)
            return result.scalars().all()