from ..service import FileUploadService
from .mocks.mock_storage_client import mock_aws_s3_client
import pytest

@pytest.mark.asyncio
async def test_upload_file():
    mock_service = FileUploadService(mock_aws_s3_client())
    response = await mock_service.upload_file("test.txt")
    assert response == "File uploaded successfully"

@pytest.mark.asyncio
async def test_download_file():
    mock_service = FileUploadService(mock_aws_s3_client())
    response = await mock_service.download_file("test.txt")
    assert response == "File downloaded successfully"

@pytest.mark.asyncio
async def test_delete_file():
    mock_service = FileUploadService(mock_aws_s3_client())
    response = await mock_service.delete_file("test.txt")
    assert response == "File deleted successfully"
