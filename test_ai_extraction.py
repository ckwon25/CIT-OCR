from app.services.ollama_client import generate

ocr_text = """
Virginia DRIVER'S LICENSE

Customer Number E66031726

KWON
CALVIN SOONHYUK

Date of Birth
04/17/2007

Exp
04/17/2031

12602 HERITAGE FARM LN
HERNDON VA 20171
"""

prompt = f"""
You are a document extraction engine.

Document Type:
drivers_license

OCR Text:
{ocr_text}

Extract:

- first_name
- last_name
- date_of_birth
- address
- document_number
- expiration_date

Return ONLY valid JSON.

No markdown.
No explanation.
No comments.
"""

result = generate(prompt)

print(result)
