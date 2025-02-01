import asyncio
import redis.asyncio as redis
from fastapi import WebSocket


class NotificationService:
    def __init__(self, redis_url: str):
        """Initialize the Redis connection for Pub/Sub notifications."""
        self.redis_url = redis_url
        self.client = redis.from_url(self.redis_url)

    async def publish_new_media(self, media_data: dict):
        """Publish a new media notification to the Redis channel."""
        await self.client.publish("new_media", str(media_data))

    async def subscribe(self, websocket: WebSocket):
        """Subscribe a WebSocket client to the notification channel."""
        pubsub = self.client.pubsub()
        await pubsub.subscribe("new_media")
        await websocket.accept()

        try:
            async for message in pubsub.listen():
                if message["type"] == "message":
                    await websocket.send_text(message["data"].decode("utf-8"))
        except Exception:
            pass
        finally:
            await pubsub.unsubscribe("new_media")
            await websocket.close()

    async def handle_message(self, websocket: WebSocket, message: str):
        """Handle incoming WebSocket messages (if needed)."""
        print(f"Received message from client: {message}")

    async def unsubscribe(self, websocket):
        pass
