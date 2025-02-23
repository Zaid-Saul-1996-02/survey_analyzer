from .utils_function.utils_function import busqueda
from langchain_core.tools import tool
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import base64

# Decodifica cada fila en base64 y conviértela en una lista de Python
def base64_to_array(base64_str):
    # Decodifica la cadena de Base64 a bytes
    byte_data = base64.b64decode(base64_str)
    # Convierte los bytes en un array de numpy (ajusta el tipo de dato si es necesario)
    return np.frombuffer(byte_data, dtype=np.float32).tolist()

@tool
def recuperador_tool(texto:str, dir_matriz:str) -> str:
    """Se llama cuando se necesita recuperar la informacion necesaria de la encuesta.
    
    Input: 
    texto:str El texto de lo que desea saber el usuario de la encuesta, ideal tenga la mayor cantidad de informacion posible
    dir_matriz:str El directorio o la url de la matriz de datos o DB que se indica en el promt del sistema
    
    Output:
    El texto resultados de la recuperacion de informacon de la encuesta a la pregunta que se realizo
    """
    print(texto, "--" ,dir_matriz)

    df = pd.read_excel(dir_matriz)
    print(df.shape)
    #df['embedding_preguntas'] = df['embedding_preguntas'].apply(eval)
    #df['embedding_respuestas'] = df['embedding_respuestas'].apply(eval)
    df['embedding_preguntas'] = df['embedding_preguntas'].apply(base64_to_array)
    df['embedding_respuestas'] = df['embedding_respuestas'].apply(base64_to_array)

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
    
    print(string_respuesta)

    return string_respuesta

tools_chat = [recuperador_tool]