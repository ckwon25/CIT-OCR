from fastapi import APIRouter, UploadFile, File
import tempfile
import os

from app.ocr.paddle_engine import extract_text
from app.classifiers.document_classifier import classify_document
from app.extractors.social_security import extract_social_security
from app.extractors.drivers_license import extract_drivers_license

router = APIRouter()


@router.post("/scan")
async def scan_document(
    file: UploadFile = File(...)
):

    suffix = os.path.splitext(file.filename)[1]

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    )

    contents = await file.read()

    temp.write(contents)
    temp.close()

    text = extract_text(temp.name)

    classification = classify_document(text)

    fields = {}

    if classification["document_type"] == "social_security_card":
        fields = extract_social_security(text)

    elif classification["document_type"] == "drivers_license":
        fields = extract_drivers_license(text)

    return {
        "document_type": classification["document_type"],
        "confidence": classification["confidence"],
        "fields": fields,
        "raw_text": text
    }