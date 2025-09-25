class Publisher:
    def __init__(self, message_broker_service) -> None:
        self.message_broker_service = message_broker_service

    async def publish(self, message: bytes, exchange_name: str, routing_key: str) -> None:
        if not self.message_broker_service.is_connected():
            raise RuntimeError("Publisher is not connected")

        await self.message_broker_service.publish(exchange_name, routing_key, message)