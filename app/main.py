from fastapi import FastAPI
from app.routes.scan import router

app = FastAPI(
    title="CIT OCR",
    version="0.1.0"
)

app.include_router(router)

@app.get("/")
def health():
    return {"status": "healthy"}