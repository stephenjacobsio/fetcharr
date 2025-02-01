from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from typing import AsyncGenerator

# Load environment variables
load_dotenv()

# Fetch database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/media_aggregator")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

# Create asynchronous database engine
engine = create_async_engine(DATABASE_URL, echo=False, future=True)

# Create a session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)

# Dependency for database session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

# Function to initialize database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Function to close database connection
async def close_db():
    await engine.dispose()