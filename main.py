from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from file_upload_service.router import router as file_upload_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    yield

app = FastAPI(lifespan=lifespan)

routers = [file_upload_router]

for router in routers:
    app.include_router(router)

