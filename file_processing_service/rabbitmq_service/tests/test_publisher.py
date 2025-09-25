from file_processing_service.rabbitmq_service.tests.mocks.mock_service import mock_rabbitmq_service
from file_processing_service.rabbitmq_service.publishers.publisher import Publisher
from pytest import mark

@mark.asyncio
async def test_publisher():
    publisher = Publisher(mock_rabbitmq_service())
    await publisher.publish(b"test_message", 'test_exchange', 'test_routing_key')