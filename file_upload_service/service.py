from .aws_s3_service import AWSS3Service
class FileUploadService:
    def __init__(self, storage_service = None):
        self.storage_service = storage_service or AWSS3Service()

    async def upload_file(self, file):
        # Logic to upload the file using the storage_service
        await self.storage_service.upload(file)

    async def download_file(self, file_key):
        # Logic to download the file using the storage_service
        await self.storage_service.download(file_key)

    async def delete_file(self, file_key):
        # Logic to delete the file using the storage_service
        await self.storage_service.delete(file_key)