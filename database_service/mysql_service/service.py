from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from pydantic import BaseModel
import os

class MySQLService:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)

    async def create_one(self, schema: DeclarativeBase, data: BaseModel) -> DeclarativeBase:
        async with self.Session() as session:
            instance = schema(**data.dict())
            session.add(instance)
            await session.commit()
            return instance
    
    async def get_one(self, schema: DeclarativeBase, id: str) -> DeclarativeBase:
        async with self.Session() as session:
            instance = await session.get(schema, id)
            return instance
    
    async def get_all(self, schema: DeclarativeBase, query: BaseModel) -> list[DeclarativeBase]:
        async with self.Session() as session:
            instances = await session.query(schema).filter_by(**query.model_dump()).all()
            return instances

    async def update_one(self, schema: DeclarativeBase, id: str, data: BaseModel) -> DeclarativeBase:
        async with self.Session() as session:
            instance = await self.get_one(schema, id)
            for key, value in data.dict().items():
                setattr(instance, key, value)
            await session.commit()
            return instance

    async def delete_one(self, schema: DeclarativeBase, id: str) -> None:
        async with self.Session() as session:
            instance = await self.get_one(schema, id)
            await session.delete(instance)
            await session.commit()
    
    async def create_metadata(self, schema: DeclarativeBase):
        async with self.Session() as session:
            schema.metadata.create_all(self.engine)

class MySQLSingleton:
    _instance = None

    def __new__(cls) -> "MySQLService":
        if cls._instance is None:
            cls._instance = MySQLService(os.getenv('DATABASE_URL', ''))
        return cls._instance