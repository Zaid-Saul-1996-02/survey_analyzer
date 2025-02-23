from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from app.core.dependencies import get_api_key
from app.schemas.shema import RequestBot
from app.services.agent.agent import agent

router = APIRouter(
    tags=["Bot de Chat"],
    dependencies=[Depends(get_api_key)],
    responses={404: {"description": "Not found"}},
)

@router.post("/bot")
async def chat_bot(request_data: RequestBot):

    print(f"\n{'='*20}")
    print("Iniciando chat bot...")
    print("="*20)

    try:
        
        user_id = request_data.user_id
        mensaje = request_data.mensaje
        url_matriz = request_data.url_matriz

        print(f"\n{'='*20}")
        print(f"user_id: {user_id} - mensaje: {mensaje}")
        print("="*20)

    except Exception as e:

        print(f"\n{'='*20}")
        print(f"Error de Parametros en el chat bot: {str(e)}")
        print("="*20)

        raise HTTPException(status_code=400, 
                            detail=str(e)
                        )
    
    try:
        text_resp = await agent(user_id, 
                                mensaje, 
                                url_matriz, 
                                ""
                            )
        
        print(f"\n{'='*20}")
        print("Chat bot completado exitosamente.")
        print("="*20)

        return JSONResponse(content={"ai_message": text_resp}, 
                            status_code=200
                        )
    
    except Exception as e:

        print(f"\n{'='*20}")
        print(f"Error de ejecucion en el chat bot: {str(e)}")
        print("="*20)

        return JSONResponse(content={"ai_message": "Lo sentimos, hubo un error"}, 
                            status_code=422
                        )