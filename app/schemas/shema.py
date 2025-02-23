from pydantic import BaseModel


class RequestDataLk(BaseModel):
    url_excel: str
    url_pdf_esquema: str
    url_pdf_context: str

class RequestBot(BaseModel):
    user_id: str
    mensaje: str
    url_matriz: str