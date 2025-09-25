class FileProcessingService:
    def __init__(self, publisher_client, consumer_client):
        self.publisher_client = publisher_client
        self.consumer_client = consumer_client

    def process_file(self, file: str):
        pass