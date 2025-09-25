from file_processing_service.rabbitmq_service.tests.mocks.mock_service import mock_rabbitmq_service
from pytest import mark

@mark.asyncio
async def test_mock_rabbitmq_service():
    mock_service = mock_rabbitmq_service()
    assert mock_service._connection is not None
    assert mock_service._channel is not None
    await mock_service.declare_queue("test_queue")
    await mock_service.declare_exchange("test_exchange", 'default')
    await mock_service.publish("test_exchange", "test_routing_key", b"test_body")
    await mock_service.consume( "test_routing_key")
    await mock_service.bind_exchange_queue( 'test_exchange', "test_routing_key")
    await mock_service.close()