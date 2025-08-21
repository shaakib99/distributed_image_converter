class Publisher:
    def __init__(self, client) -> None:
        self.client = client

    def publish(self, message: str, exchange_name: str, routing_key: str) -> None:
        if not self.client.is_connected():
            raise RuntimeError("Publisher is not connected")
        
        exchange = self.client.get_exchange(exchange_name)
        exchange.publish(message, exchange, routing_key)