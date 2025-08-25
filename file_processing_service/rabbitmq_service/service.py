
from aio_pika import connect_robust, Message
import os


class RabbitMQService:
    def __init__(self) -> None:
        self._connection = None
        self._channel = None
        self.uri = os.getenv("RABBITMQ_URI", "amqp://guest:guest@localhost/")

    async def connect(self) -> None:
        self._connection = await connect_robust(self.uri)
        self._channel = await self._connection.channel()

    async def publish(self, target_exchange: str, routing_key: str, body: bytes) -> None:
        if not self._channel:
            raise RuntimeError("Publisher is not connected")
        exchange = await self._channel.get_exchange(target_exchange)
        await exchange.publish(Message(body), routing_key=routing_key)

    async def consume(self, queue_name: str, auto_ack=True, on_message = lambda x: x) -> None:
        if not self._channel:
            raise RuntimeError("Consumer is not connected")
        queue = await self._channel.get_queue(queue_name)
        await queue.consume(callback=on_message, no_ack=auto_ack)

    async def declare_queue(self, queue_name: str) -> None:
        if not self._channel:
            raise RuntimeError("Publisher is not connected")
        await self._channel.declare_queue(queue_name)
    
    async def declare_exchange(self, exchange_name: str, exchange_type: str) -> None:
        if not self._channel:
            raise RuntimeError("Publisher is not connected")
        await self._channel.declare_exchange(exchange_name, exchange_type)

    async def bind_exchange_queue(self, exchange_name: str, queue_name: str) -> None:
        if not self._channel:
            raise RuntimeError("Publisher is not connected")
        exchange = await self._channel.get_exchange(exchange_name)
        if exchange is None:
            raise ValueError(f"Exchange '{exchange_name}' not found")
        queue = await self._channel.get_queue(queue_name)
        if queue is None:
            raise ValueError(f"Queue '{queue_name}' not found")
        await queue.bind(exchange)

    async def close(self) -> None:
        if self._channel:
            await self._channel.close()
        if self._connection:
            await self._connection.close()

class RabbitMQServiceSingleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = RabbitMQService()
        return cls._instance