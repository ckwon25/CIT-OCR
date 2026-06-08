from pydantic import BaseModel


class DocumentResult(BaseModel):
    document_type: str
    confidence: float
    fields: dict
