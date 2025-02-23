from openai import OpenAI
from .prompts import (
    system_message_get_capitulo, 
    system_message_extraccion_datos,
    system_message_categorizar_clasificar,
    system_message_analisis_1,
    system_message_por_que,
    system_message_informe
)

# Obtener capitulo ================================ 

def get_capitulo(
        texto_capitulo:str, 
        texto_estructura:str
) -> str:
    
    client = OpenAI()

    user_message = f"""Extrae la estrcutura de capitulo correspondiente:  
1. **Texto de Capítulo de Entrevista**:  
{texto_capitulo}  

2. **Texto de Estructuras de Capítulos**:  
{texto_estructura}  
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message_get_capitulo},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0,
            max_tokens=4096,
            seed = 250
            )

        respuesta = response.choices[0].message.content

        return respuesta
    except:
        return ""

# Extraccion de datos ================================

def extraccion_datos(
        texto_contexto:str, 
        texto_objetivo:str, 
        texto_subcapitulo:str
) -> str:
    
    client = OpenAI()


    user_message = f"""Realiza el informe para los siguinetes documentos de texto:  
1. **Contexto:**  
{texto_contexto}  

2. **Objetivo del sucapitulo:**  
{texto_objetivo}  

3. **Subcapítulo:**  
{texto_subcapitulo}  
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message_extraccion_datos},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0,
            max_tokens=4096,
            seed = 250
            )

        respuesta = response.choices[0].message.content

        return respuesta
    except:
        return ""
    
# Categorizar/Clasificar ================================

def categorizar_clasificar(
        texto_contexto:str, 
        texto_objetivo:str, 
        texto_subcapitulo:str, 
        texto_extraccion_datos:str, 
        texto_datos_personales:str
) -> str:
    
    client = OpenAI()

    user_message = f"""Realiza el informe para los siguinetes documentos de texto:  
1. **Contexto:**  
{texto_contexto}  

2. **Objetivo del sucapitulo:**  
{texto_objetivo}  

3. **Subcapítulo:**  
{texto_subcapitulo}  

4. **Extraccion de datos:**  
{texto_extraccion_datos}  

5.  **Caracterizacion de usuarios:**  
{texto_datos_personales}  
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message_categorizar_clasificar},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0,
            max_tokens=4096,
            seed = 250
            )

        respuesta = response.choices[0].message.content

        return respuesta
    except:
        return ""
    
# Analisis 1 ================================

def analisis_1(
        texto_contexto:str, 
        texto_objetivo:str,
        texto_subcapitulo:str, 
        texto_extraccion_datos:str, 
        texto_categorizar_clasificar:str
) -> str:

    client = OpenAI()

    
    user_message = f"""Realiza el informe para los siguinetes documentos de texto:  
1. **Contexto:**  
{texto_contexto}  

2. **Objetivo del sucapitulo:**  
{texto_objetivo}  

3. **Subcapítulo:**  
{texto_subcapitulo}  

4. **Extraccion de datos:**  
{texto_extraccion_datos}  

5. **CATEGORIZACION/CLASIFICACION y caracterizacion:**  
{texto_categorizar_clasificar}  
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message_analisis_1},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=4096,
            )

        respuesta = response.choices[0].message.content

        return respuesta
    except:
        return ""
    
# Por que ================================

def refact_porque(texto_analisis_subcapitulo:str) -> str:

    client = OpenAI()

    user_message = f"""Realiza el analisis para el siguiente texto:  
{texto_analisis_subcapitulo}  
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message_por_que},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=4096,
            )

        respuesta = response.choices[0].message.content

        return respuesta
    except:
        return ""
    
# Informe ================================

def informe(texto_analisis_subcapitulo:str) -> str:

    client = OpenAI()

    
    user_message = f"""Realiza el analisis sobre toda esta informacion que se te entrega:    
{texto_analisis_subcapitulo}  
"""

    user_message_2 = "Necesito que dupliques la extensión del informe que creaste, extendiendo los argumentos, siendo más detallado y profesional, recuerda siempre limitar tu contexto a la información que te fue proporcionada"

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message_informe},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3,
            max_tokens=4096,
            seed = 250
            )

        respuesta_1 = response.choices[0].message.content

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message_informe},
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": respuesta_1},
                {"role": "user", "content": user_message_2}
            ],
            temperature=0.3,
            max_tokens=4096,
            seed = 250
            )
        
        respuesta_2 = response.choices[0].message.content

        return respuesta_1, respuesta_2
    except:
        return "", ""
