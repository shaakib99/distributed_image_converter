from unittest.mock import AsyncMock, patch
from .mocks.mock_database_service import mock_database_service
import pytest

@pytest.mark.asyncio
async def test_create_one():
    database_service = mock_database_service()
    await database_service.create_one({'test': 'test'})

@pytest.mark.asyncio
async def test_update_one():
    database_service = mock_database_service()
    await database_service.update_one('test', {'test': 'test'})

@pytest.mark.asyncio
async def test_get_one():
    database_service = mock_database_service()
    await database_service.get_one('test')

@pytest.mark.asyncio
async def test_delete_one():
    database_service = mock_database_service()
    await database_service.delete_one('test')

@pytest.mark.asyncio
async def test_get_all():
    database_service = mock_database_service()
    await database_service.create_one({'test': 'test'})