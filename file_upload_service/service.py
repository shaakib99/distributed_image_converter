from .aws_s3_client import AWSS3Client
class FileUploadService:
    def __init__(self, storage_client = None):
        self.storage_client = storage_client or AWSS3Client()

    async def upload_file(self, file):
        return await self.storage_client.upload(file)

    async def download_file(self, file_key):
        return await self.storage_client.download(file_key)

    async def delete_file(self, file_key):
        return await self.storage_client.delete(file_key)