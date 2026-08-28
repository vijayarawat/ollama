import requests

response = requests.post(
    "https://ollama-2-sl2c.onrender.com/api/generate",
    json={
        "model": "qwen2:0.5b",
        "prompt": "Explain Redis caching",
        "stream": False
    },
    timeout=180
)

print(response.json())



