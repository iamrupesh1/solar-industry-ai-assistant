import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_URL = os.getenv("HF_API_URL")
HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_URL or not HF_API_KEY:
    print("Set HF_API_URL and HF_API_KEY in .env file first.")
    exit(1)

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "inputs": "Hello, test AI inference!"
}

response = requests.post(HF_API_URL, headers=headers, json=payload)

if response.status_code == 200:
    print("API call successful:")
    print(response.json())
else:
    print(f"API call failed with status {response.status_code}: {response.text}")
