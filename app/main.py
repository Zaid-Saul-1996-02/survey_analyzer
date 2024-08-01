from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import Dict
from fastapi.responses import JSONResponse
import uvicorn
import os
from dotenv import load_dotenv

from core.analisis_general import analisis_general

load_dotenv()

app = FastAPI()

API_KEY_AUTH = os.getenv('API_KEY_AUTH')

if API_KEY_AUTH is None:
    raise Exception("API_KEY_AUTH not configured in .env file")

def get_api_key(api_key_auth: str = Header(...)):
    if api_key_auth != API_KEY_AUTH:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return api_key_auth

class RequestDataLk(BaseModel):
    url_excel: str
    url_pdf_esquema: str
    url_pdf_context: str

@app.post("/analizar")
async def analizar_matriz(request_data: RequestDataLk, api_key_auth: str = Depends(get_api_key)):
    try:
        url_excel = request_data.url_excel
        url_pdf_esquema = request_data.url_pdf_esquema
        url_pdf_context = request_data.url_pdf_context

        print('Hola')

        resultado = analisis_general(url_excel, url_pdf_esquema, url_pdf_context)

        print('entro')

        return JSONResponse(content={"data": resultado}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#uvicorn main:app --reload