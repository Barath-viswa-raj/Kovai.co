import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://apihub.document360.io/v2/Drive/Folders"

def get_headers():
    return {
        "Content-Type": "application/json",
        "api_token": os.getenv("API_TOKEN", "mock_token")
    }
