from unittest.mock import AsyncMock, patch

@patch('database_service.mysql_service.service.MySQLService')
def mock_mysql_service(MySQLService):
    mysql_service = MySQLService
    mysql_service.create_one = AsyncMock(return_value='success')
    mysql_service.update_one = AsyncMock(return_value='success')
    mysql_service.delete_one = AsyncMock(return_value='success')
    mysql_service.get_one = AsyncMock(return_value='success')
    mysql_service.get_all = AsyncMock(return_value='success')

    return mysql_service