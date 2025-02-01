from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional, Any, Coroutine, Sequence
from src.core.models.movie import Movie

class MovieRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_movies(self) -> Sequence[Movie]:
        """Retrieve all movies from the database."""
        result = await self.db.execute(select(Movie))
        return result.scalars().all()

    async def get_movie_by_id(self, movie_id: int) -> Optional[Movie]:
        """Retrieve a movie by its ID."""
        result = await self.db.execute(select(Movie).where(Movie.id == movie_id))
        return result.scalar_one_or_none()

    async def add_movie(self, movie: Movie) -> None:
        """Add a new movie to the database."""
        self.db.add(movie)
        await self.db.commit()

    async def delete_movie(self, movie_id: int) -> None:
        """Delete a movie by its ID."""
        movie = await self.get_movie_by_id(movie_id)
        if movie:
            await self.db.delete(movie)
            await self.db.commit()