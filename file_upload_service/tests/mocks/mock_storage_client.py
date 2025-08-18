from unittest.mock import AsyncMock, patch

@patch("file_upload_service.aws_s3_client.AWSS3Client")
def mock_aws_s3_client(mock_client):
    mock_client.upload = AsyncMock(return_value="File uploaded successfully")
    mock_client.download = AsyncMock(return_value="File downloaded successfully")
    mock_client.delete = AsyncMock(return_value="File deleted successfully")
    return mock_client