import json


def build_extraction_prompt(
    document_type: str,
    ocr_text: str
):

    return f"""
You are a document extraction engine.

Document Type:
{document_type}

OCR Text:
{ocr_text}

Extract all available fields.

Return ONLY valid JSON.

Schema:

{{
    "document_type": "{document_type}",
    "fields": {{
        "first_name": "",
        "last_name": "",
        "middle_name": "",
        "date_of_birth": "",
        "address": "",
        "document_number": "",
        "expiration_date": "",
        "issue_date": ""
    }}
}}

Rules:

- Do not invent data.
- Use null if unavailable.
- Normalize dates to YYYY-MM-DD.
- Return JSON only.
"""
