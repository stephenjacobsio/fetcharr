from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from src.services.notification_service import NotificationService
from src.config import Settings

router = APIRouter()

# Initialize notification service
settings = Settings()
notification_service = NotificationService(settings.REDIS_URL)

@router.websocket("/ws")
async def websocket_notifications(websocket: WebSocket):
    """WebSocket endpoint for real-time notifications."""
    await notification_service.subscribe(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await notification_service.handle_message(websocket, data)
    except WebSocketDisconnect:
        await notification_service.unsubscribe(websocket)