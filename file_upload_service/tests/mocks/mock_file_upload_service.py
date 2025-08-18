from unittest.mock import AsyncMock, patch
from .mock_storage_client import mock_aws_s3_client
from ...service import FileUploadService

def mock_file_upload_service():
    mock_service =  FileUploadService(mock_aws_s3_client())
    mock_service.upload_file = AsyncMock(return_value="File uploaded successfully")
    mock_service.download_file = AsyncMock(return_value="File downloaded successfully")
    mock_service.delete_file = AsyncMock(return_value="File deleted successfully")
    return mock_service