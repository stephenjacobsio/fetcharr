from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.metadata_service import MetadataService
from src.core.database import get_db

router = APIRouter()

def get_metadata_service(db: AsyncSession = Depends(get_db)):
    return MetadataService(db)

@router.get("/{title}")
async def get_metadata(
    title: str,
    metadata_service: MetadataService = Depends(get_metadata_service)
):
    """Fetch metadata for a given title from multiple providers."""
    try:
        return await metadata_service.fetch_metadata(title)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/enrich")
async def enrich_metadata(
    title: str,
    metadata_service: MetadataService = Depends(get_metadata_service)
):
    """Enrich existing metadata with additional details from external providers."""
    try:
        return await metadata_service.enrich_metadata(title)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))