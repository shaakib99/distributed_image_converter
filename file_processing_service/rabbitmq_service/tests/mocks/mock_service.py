from unittest.mock import AsyncMock, Mock
from file_processing_service.rabbitmq_service.service import RabbitMQService
from file_processing_service.rabbitmq_service.service import connect_robust

def mock_rabbitmq_service():
    mock_service = RabbitMQService()
    mock_service.is_connected = Mock(return_value=True)
    mock_connection = AsyncMock()
    mock_channel = AsyncMock()
    mock_channel.get_exchange = AsyncMock()
    mock_channel.get_queue = AsyncMock()
    mock_channel.declare_queue = AsyncMock()
    mock_channel.declare_exchange = AsyncMock()
    mock_channel.close = AsyncMock()
    mock_connection.channel = AsyncMock(return_value=mock_channel)

    mock_service._connection = mock_connection
    mock_service._channel = mock_channel
    return mock_service