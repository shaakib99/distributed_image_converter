class Publisher:
    def __init__(self, client) -> None:
        self.client = client

    async def publish(self, message: str, exchange_name: str, routing_key: str) -> None:
        if not self.client.is_connected():
            raise RuntimeError("Publisher is not connected")
        
        exchange = await self.client.get_exchange(exchange_name)
        await exchange.publish(message, routing_key)