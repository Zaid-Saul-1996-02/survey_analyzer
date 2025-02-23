import requests
import numpy as np
import pandas as pd
import fitz
from openai import OpenAI
import io

def pdf_to_text(pdf_url:str) -> list:
    # Descargar el PDF desde la URL
    try:
        response = requests.get(pdf_url)

        if response.status_code == 200:
            pdf_stream = io.BytesIO(response.content)

            texto = ""
            doc = fitz.open(stream=pdf_stream, filetype="pdf")
            for page in doc:
                texto += page.get_text()
            return texto
        else:
            return ""
    except:
        return ''
    
def get_embedding(text, model="text-embedding-3-large"):
   client = OpenAI()
   text = text.lower().replace("\n", " ")
   #print(text)
   return client.embeddings.create(input = [text], model=model).data[0].embedding

def similitud_coseno(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def distance_euclidean(v,w):
    v = np.array(v)
    w = np.array(w)

    d = v - w
    
    return (d @ d) ** (1/2)

def busqueda(df:pd.DataFrame, texto:str, column:str = 'embedding_preguntas', n:int = 2):

    t = get_embedding(texto)

    df['similitud'] = df[column].apply(lambda x: distance_euclidean(x,t))

    res = df.sort_values('similitud', ascending=True).head(2)

    return res