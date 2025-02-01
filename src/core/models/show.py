import sqlalchemy
from src.core.models.base import Base

class Show(Base):
    __tablename__ = "shows"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    tmdb_id = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    imdb_rating = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    tvdb_id = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    genres = sqlalchemy.Column(sqlalchemy.String, nullable=True)
