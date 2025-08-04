from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel

class DatabaseService:
    def __init__(self, schema: DeclarativeBase):
        self.schema = schema
    
    async def create_one(self, data: BaseModel)-> DeclarativeBase:
        pass

    async def get_one(self, data: BaseModel)-> DeclarativeBase:
        pass

    async def get_all(self, query: BaseModel)-> list[DeclarativeBase]:
        pass

    async def update_one(self, id: str, data: BaseModel)-> DeclarativeBase:
        pass

    async def delete_one(self, id: str)-> None:
        pass