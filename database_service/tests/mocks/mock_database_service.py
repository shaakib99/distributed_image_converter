from unittest.mock import AsyncMock
from .mock_mysql_service import mock_mysql_service
from database_service.service import DatabaseService

def mock_database_service():
    database_service = DatabaseService(None, mock_mysql_service())
    return database_service