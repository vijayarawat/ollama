import requests

response = requests.post(
    "https://ollama-1-3hol.onrender.com/api/generate",
    json={
        "model": "llama3.2:1b",
        "prompt": "Explain Redis caching",
        "stream": False
    },
    timeout=180
)

print(response.json())