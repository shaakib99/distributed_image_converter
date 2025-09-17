from functools import wraps
from aio_pika.abc import AbstractIncomingMessage
from file_processing_service.rabbitmq_service.service import RabbitMQServiceSingleton
from collections import defaultdict

workers_map = defaultdict(set)

def worker(routing_key: str):
    def decorator(func):
        workers_map[routing_key].add(func)
    return decorator

@worker('process_image')
async def process_message(message: AbstractIncomingMessage) -> None:
    # Process the incoming message
    print(f"Received message: " + message.body.decode())