from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from file_upload_service.router import router as file_upload_router
from file_processing_service.rabbitmq_service.service import RabbitMQServiceSingleton
from file_processing_service.rabbitmq_service.consumers.consumer import workers_map
from loggin_service.service import get_logger

logger = get_logger("main")
get_logger("uvicorn.error").disabled = True

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting application...")
    load_dotenv()
    rabbitmq_service = RabbitMQServiceSingleton()
    logger.info("Connecting to RabbitMQ...")
    await rabbitmq_service.connect()
    logger.info("Connected to RabbitMQ")

    logger.info("Declaring queues and starting consumers...")
    await rabbitmq_service.connect()
    for routing_key, workers in workers_map.items():
        await rabbitmq_service.declare_queue(routing_key)
        for worker in workers:
            await rabbitmq_service.consume(routing_key, on_message=worker)
    logger.info("Consumers are running")
    logger.info("RabbitMQ service is ready")
    logger.info("Application startup complete")
    yield
    logger.info("Shutting down application...")
    await rabbitmq_service.close()
    logger.info("Application shutdown complete")

app = FastAPI(lifespan=lifespan)

routers = [file_upload_router]

for router in routers:
    app.include_router(router)

