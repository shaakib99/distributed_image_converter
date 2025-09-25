from file_processing_service.rabbitmq_service.publishers.publisher import Publisher
from file_processing_service.rabbitmq_service.tests.mocks.mock_service import mock_rabbitmq_service

def mock_publisher():
    return Publisher(mock_rabbitmq_service)