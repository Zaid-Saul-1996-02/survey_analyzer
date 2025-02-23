from dotenv import load_dotenv
from os import getenv
from fastapi import HTTPException, Header

load_dotenv()

API_KEY_AUTH = getenv('API_KEY_AUTH')

if API_KEY_AUTH is None:
    raise Exception("API_KEY_AUTH not configured in .env file")

def get_api_key(api_key_auth: str = Header(...)):
    if api_key_auth != API_KEY_AUTH:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return api_key_auth