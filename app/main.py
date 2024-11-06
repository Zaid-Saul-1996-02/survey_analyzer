from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import Dict
from fastapi.responses import JSONResponse
import uvicorn
import os
from dotenv import load_dotenv

from core.analisis_general import analisis_general
from agent.agent import agent

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
    
class RequestBot(BaseModel):
    user_id: str
    mensaje: str
    url_matriz: str


@app.post("/bot")
async def chat_bot(request_data: RequestBot, api_key_auth: str = Depends(get_api_key)):
    try:

        user_id = request_data.user_id
        mensaje = request_data.mensaje
        url_matriz = request_data.url_matriz

        text_resp = agent(user_id, mensaje, url_matriz, "")

        return JSONResponse(content={"ai_message": text_resp}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"ai_message": "Lo sentimos, hubo un error"}, status_code=422)

    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#uvicorn main:app --reload