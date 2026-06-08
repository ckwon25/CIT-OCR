from fastapi import APIRouter, UploadFile

router = APIRouter()

@router.post("/scan")
async def scan_document(file: UploadFile):

    return {
        "filename": file.filename,
        "document_type": "unknown",
        "fields": {}
    }