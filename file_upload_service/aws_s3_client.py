import boto3
import os
import asyncio

class AWSS3Client:
    def __init__(self):
        self.s3_client = boto3.client("s3", 
                                       aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                                       aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))

    async def upload(self, file):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, lambda: self.s3_client.upload_fileobj(file.file, os.getenv("S3_BUCKET_NAME"), f"{file.filename}"))

    async def download(self, file_key):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, lambda: self.s3_client.get_object(Bucket=os.getenv("S3_BUCKET_NAME"), Key=file_key))

    async def delete(self, file_key):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, lambda: self.s3_client.delete_object(Bucket=os.getenv("S3_BUCKET_NAME"), Key=file_key))