from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional, Any, Coroutine, Sequence
from src.core.models.show import Show

class ShowRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_shows(self) -> Sequence[Show]:
        """Retrieve all shows from the database."""
        result = await self.db.execute(select(Show))
        return result.scalars().all()

    async def get_show_by_id(self, show_id: int) -> Optional[Show]:
        """Retrieve a show by its ID."""
        result = await self.db.execute(select(Show).where(Show.id == show_id))
        return result.scalar_one_or_none()

    async def add_show(self, show: Show) -> None:
        """Add a new show to the database."""
        self.db.add(show)
        await self.db.commit()

    async def delete_show(self, show_id: int) -> None:
        """Delete a show by its ID."""
        show = await self.get_show_by_id(show_id)
        if show:
            await self.db.delete(show)
            await self.db.commit()