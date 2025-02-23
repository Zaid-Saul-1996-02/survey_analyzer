from fastapi import FastAPI, Depends
from app.core.dependencies import get_api_key

from app.routers import (
    analisis,
    agent
)

app = FastAPI()

app.include_router(analisis.router)
app.include_router(agent.router)

@app.get("/")
async def root():

    print(f"\n{'='*20}")
    print("Iniciando API...")
    print("="*20)
    
    return {"message": "Hello, welcome to the API of Survey Analyzer"}