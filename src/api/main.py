from fastapi import FastAPI
from src.api.routes import (
    jellyfin,
    radarr,
    sonarr,
    metadata,
    watch_history,
    filters,
    analytics,
    notifications
)

# Create FastAPI app instance
app = FastAPI(
    title="FetchArr",
    description="Metadata Aggregator for Media Libraries",
    version="1.0.0"
)

# Include routers
app.include_router(jellyfin.router, prefix="/jellyfin", tags=["Jellyfin"])
app.include_router(radarr.router, prefix="/radarr", tags=["Radarr"])
app.include_router(sonarr.router, prefix="/sonarr", tags=["Sonarr"])
app.include_router(metadata.router, prefix="/metadata", tags=["Metadata"])
app.include_router(watch_history.router, prefix="/watch-history", tags=["Watch History"])
app.include_router(filters.router, prefix="/filters", tags=["Filters"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])