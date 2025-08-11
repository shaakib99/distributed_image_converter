from fastapi import APIRouter, UploadFile
from .service import FileUploadService

router = APIRouter(prefix="/files")

@router.put('/upload')
async def upload_file(file: UploadFile):
    file_upload_service = FileUploadService()
    await file_upload_service.upload_file(file)
    return {"message": "File uploaded successfully"}