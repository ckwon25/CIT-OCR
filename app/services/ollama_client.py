import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate(prompt, model="qwen3:8b"):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]
