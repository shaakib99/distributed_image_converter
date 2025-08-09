from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel
from .mysql_service.service import MySQLSingleton

class DatabaseService:
    def __init__(self, schema: DeclarativeBase, database = None):
        self.schema = schema
        self.database = database or MySQLSingleton()
    
    async def create_one(self, data: BaseModel)-> DeclarativeBase:
        return await self.database.create_one(self.schema, data)

    async def get_one(self, id: str)-> DeclarativeBase:
        return await self.database.get_one(self.schema, id)

    async def get_all(self, query: BaseModel)-> list[DeclarativeBase]:
        return await self.database.get_all(self.schema, query)

    async def update_one(self, id: str, data: BaseModel)-> DeclarativeBase:
        return await self.database.update_one(self.schema, id, data)

    async def delete_one(self, id: str)-> None:
        return await self.database.delete_one(self.schema, id)