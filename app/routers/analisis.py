from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from app.core.dependencies import get_api_key
from app.schemas.shema import RequestDataLk
from app.services.analisis.analisis_general import analisis_general

router = APIRouter(
    tags=["Analisis Encuestas"],
    dependencies=[Depends(get_api_key)],
    responses={404: {"description": "Not found"}},
)

@router.post("/analizar")
async def analizar_matriz(request_data: RequestDataLk):

    print(f"\n{'='*20}")
    print("Iniciando analizar...")
    print("="*20)
    
    try:
        url_excel = request_data.url_excel
        url_pdf_esquema = request_data.url_pdf_esquema
        url_pdf_context = request_data.url_pdf_context

        print(f"\n{'='*20}")
        print(f"url_excel: {url_excel}")
        print(f"url_pdf_esquema: {url_pdf_esquema}")
        print(f"url_pdf_context: {url_pdf_context}")
        print("="*20)
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    try:
        resultado = analisis_general(url_excel, 
                                     url_pdf_esquema, 
                                     url_pdf_context
                                    )
        
        print(f"\n{'='*20}")
        print("Análisis completado exitosamente.")
        print("="*20)

        return JSONResponse(content={"data": resultado}, status_code=200)
    except Exception as e:
        print(f"\n{'='*20}")
        print(f"Error en el análisis: {str(e)}")
        print("="*20)

        raise HTTPException(status_code=500, detail=str(e))