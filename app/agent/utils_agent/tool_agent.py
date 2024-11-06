from .utils_function.utils_function import busqueda
from langchain_core.tools import tool
import pandas as pd
import numpy as np


@tool
def recuperador_tool(texto:str, dir_matriz:str) -> str:
    """Se llama cuando se necesita recuperar la informacion necesaria de la encuesta.
    
    Input: 
    texto:str El texto de lo que desea saber el usuario de la encuesta, ideal tenga la mayor cantidad de informacion posible
    dir_matriz:str El directorio o la url de la matriz de datos o DB que se indica en el promt del sistema
    
    Output:
    El texto resultados de la recuperacion de informacon de la encuesta a la pregunta que se realizo
    """
    #print(texto, "--" ,dir_matriz)

    df = pd.read_csv(dir_matriz)
    df['embedding_preguntas'] = df['embedding_preguntas'].apply(eval)
    df['embedding_respuestas'] = df['embedding_respuestas'].apply(eval)

    bus_preg = busqueda(df, texto)
    bus_resp = busqueda(df, texto, column='embedding_respuestas')

    df_bus = pd.concat([bus_preg, bus_resp])
    df_bus.sort_values('similitud', ascending=True, inplace=True)

    string_respuesta = f"""
## Respuestas recuperadas 1
**Pregunta: ** {df_bus.iloc[0,0]}  
**Respuestas de los usuarios:**  
{df_bus.iloc[0, 1]}

## Respuestas recuperadas 2
**Pregunta: ** {df_bus.iloc[1,0]}  
**Respuestas de los usuarios:**  
{df_bus.iloc[1, 1]}
"""

    return string_respuesta

tools_chat = [recuperador_tool]