from openai import OpenAI

def get_capitulo(texto_capitulo:str, texto_estructura:str) -> str:
    
    client = OpenAI()

    system_message = """Eres un experto en análisis de textos especializado en identificar y extraer exclusivamente la estructura de un único capítulo de entrevistas basado en su contenido y numeración específica.

    ### **Datos Recibidos**:  
    1. **Texto de Capítulo de Entrevista**: Contiene la estructura de un capítulo sin enumerar.  
    2. **Texto de Estructuras de Capítulos**: Incluye las diferentes estructuras de capítulos de un informe, detallando títulos y subsecciones.  

    ### **Pasos a Seguir**:  
    1. Leer y comprender detenidamente ambos textos.  
    2. Comparar el contenido del Texto de Capítulo de Entrevista con las estructuras en el Texto de Estructuras de Capítulos.  
    3. Identificar y seleccionar únicamente la estructura del capítulo que coincida con el contenido del Texto de Capítulo de Entrevista.  
    4. Asegurarse de incluir todas las subsecciones y detalles correspondientes a ese capítulo específico, comenzando con su numeración (por ejemplo, "3.").  
    5. Excluir cualquier subsección o contenido que no pertenezca al capítulo identificado (por ejemplo, numeraciones como "4.", "5.", etc.).  

    ### **Respuesta Requerida**:  
    - Debes devolver la estructura completa del capítulo identificado, incluyendo todas sus subsecciones y detalles que comiencen con la misma numeración de capítulo.  
    - No debes incluir información de otros capítulos ni ninguna explicación adicional.  

    ### **Nota Final**:  
    Es crucial que no incluyas información o texto adicional en tu respuesta. Debes devolver exclusivamente la estructura del capítulo identificado, sin añadir comentarios, explicaciones ni textos que no formen parte directa de la estructura del capítulo especificado. Concentra tu respuesta únicamente en los elementos estructurales como títulos y subsecciones que comienzan con el número de capítulo correspondiente.
    """

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
                {"role": "system", "content": system_message},
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
    


def extraccion_datos(texto_contexto:str, texto_objetivo:str, texto_subcapitulo:str) -> str:
    
    client = OpenAI()

    system_message = """**Eres un analista altamente especializado en estudios cualitativos.** Tu tarea principal consiste en realizar un análisis profundo mediante la extraccion de datos de un subcapítulo específico dentro de un capítulo de una encuesta que abarca preguntas diversas sobre marcas o productos específicos y lo que responden los entrevistados a esas preguntas. Tu análisis debe realizarse según el **Objetivo del subcapítulo** y del estudio. Utilizarás documentos clave adaptados a cada segmento del análisis, siempre considerando el objetivo de análisis en el subcapítulo.  

    **Documentos proporcionados para el análisis:**  
    A continuación, se detallan los textos que se emplearán para facilitar tu análisis. Tu enfoque estará en el subcapítulo específico dado; los documentos siguientes te servirán de referencia para comprender el contexto y estructura relevantes:  

    - **Contexto:** Ofrece antecedentes, objetivos estratégicos y las razones fundamentales detrás de la encuesta completa. Este documento te ayudará a comprender el propósito global de la encuesta y te servirá como referencia para situar el análisis.

    - **Objetivo del subcapítulo:** Ofrece lo que se busca analizar o saber en el **Subcapítulo**. Todo el análisis debe basarse en este objetivo, pues es lo que se busca entender. Los análisis deben responder a este objetivo.

    - **Subcapítulo:** Este es el texto principal que deberás analizar para extraer datos detalladamente, basándote siempre en el **Objetivo del subcapítulo** a la hora de extraer los datos. Este contiene las preguntas realizadas a los entrevistados y sus respuestas correspondientes al estudio realizado, que es la información principal de análisis sobre la que se realiza el estudio.

    **Pasos a seguir:**  
    - Lee detenidamente toda la información del **Subcapítulo** y a la vez ve extrayendo: palabras e ideas clave, como una lluvia de ideas, y a medida que se extraen estas ideas, marca el número de repeticiones de cada una. Esto nos permite saber cuáles ideas tienen más impacto en el **Objetivo del subcapítulo** a responder y cuales menor impacto.  

    **Nota:** Es crucial que sigas meticulosamente este paso para llevar a cabo una extraccion de datos exhaustiva del subcapítulo. Asegúrate de emplear **verbatims** constantemente para sustentar tus análisis de manera efectiva, ilustrando claramente las tendencias y opiniones presentes en el subcapítulo, siempre tener en cuenta el **Objetivo del subcapítulo**.  

    Solo responde con el resultado de la extraccion de datos y no des información de antecedentes ni nada similar, tampoco des encabezados de nombre del capitulo ni cunclusiones preliminares, solo dame el resultado de los pasos indicados.  
    """
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
                {"role": "system", "content": system_message},
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
    

def categorizar_clasificar(texto_contexto:str, texto_objetivo:str, texto_subcapitulo:str, texto_extraccion_datos:str, texto_datos_personales:str) -> str:
    
    client = OpenAI()

    system_message = """**Eres un analista altamente especializado en estudios cualitativos.** Tu tarea principal consiste en CATEGORIZAR/CLASIFICAR y CARACTERIZAR resultados de un análisis de extraccion de datos realizados sobre un subcapítulo específico dentro de un capítulo de una encuesta que abarca preguntas diversas sobre marcas o productos específicos y lo que responden los entrevistados a esas preguntas. Tu análisis debe realizarse según el objetivo particular del estudio. Utilizarás documentos clave adaptados a cada segmento del análisis, siempre considerando el objetivo de análisis en el subcapítulo.  

    **Documentos proporcionados para el análisis:**  
    A continuación, se detallan los textos que se emplearán para facilitar tu análisis. Tu enfoque estará basado prinicpalmente en los documentos **Extraccion de datos**, **Subcapítulo** y **Objetivo del subcapítulo**; los documentos siguientes te servirán de referencia para comprender el contexto y estructura relevantes:  

    - **Contexto:** Ofrece antecedentes, objetivos estratégicos y las razones fundamentales detrás de la encuesta completa. Este documento te ayudará a comprender el propósito global de la encuesta y te servirá como referencia pero no es un documento escencial para el analisis.  

    - **Objetivo del subcapítulo:** Ofrece lo que se busca analizar o saber en el **Subcapítulo**. Todo el análisis debe basarse en este objetivo, pues es lo que se busca entender. Los análisis deben responder a este objetivo.  

    - **Subcapítulo:** Este contiene las preguntas realizadas a los entrevistados y sus respuestas correspondientes respecto estudio realizado en el subcapitulo.  

    - **Extraccion de datos:** Muestra un analisis preliminar realizado sobre el **Subcapítulo:** en el que se extrageron palabras e ideas clave, como una lluvia de ideas marcando el número de repeticiones de cada una. Esto nos permite saber cuáles ideas tienen más impacto en el objetivo a responder y así nos podemos enfocar en estas a la hora de realizar el análisis explicativo.  

    - **Caracterizacion de usuarios:** Este txto muestra las caracteristicas de los entrevistadas correspondientes, edad, ocupacion, etc, los datos de caracterizacion vienen dados en el mismo orden en que los entrevistados responden en el texto del **Subcapitulo**.  


    **Pasos a seguir:**  
    Teniendo en cuenta los resultados obtenidos en el documento **Extraccion de datos** obtenidos del analisis descrito sobre el documento **Subcapítulo** y teniendo siempre en cuenta el **Objetivo del subcapítulo** que se busca responder debes realizar los siguinetes pasos:  
    - Crear categorías, que permitan entender de manera más simple los resultados, según las características de cada grupo de palabras/ideas. Además, la generación de categorías debe permitir tener una idea clara de cómo vamos a plasmar los resultados.  
    - CARACTERIZAR: Es la explicación de cada categoría utilizada para responder al **Objetivo del subcapítulo**, desarrolla cada idea.  

    Al realizar el proceso, es importante notar si hay diferencias entre los diferentes segmentos evaluados en el estudio, para esta diferencia de segmentos debes basarte en la **Caracterizacion de usuarios:**, sus edades, ocupaciones, etc. Esto es clave porque nuestro cliente, debe ejecutar estrategias distintas según el target al que se está dirigiendo, por lo que es importante hacerle evidente si sus tipos de clientes/segmentos muestran diferencias en sus opiniones o comportamientos.  

    **Nota:** Es crucial que sigas meticulosamente este paso para llevar a cabo una extraccion de datos exhaustiva del subcapítulo. Asegúrate de emplear **verbatims** constantemente para sustentar tus análisis de manera efectiva, ilustrando claramente las tendencias y opiniones presentes en el subcapítulo, siempre tener en cuenta el **Objetivo del subcapítulo**.  

    Solo responde con el resultado de los pasos indicados y no des información de antecedentes ni nada similar, tampoco des encabezados de nombre del capitulo ni cunclusiones preliminares, solo dame el resultado de los pasos indicados.  
    """
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
                {"role": "system", "content": system_message},
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
    

def analisis_1(texto_contexto:str, texto_objetivo:str, texto_subcapitulo:str, texto_extraccion_datos:str, texto_categorizar_clasificar:str) -> str:

    client = OpenAI()

    system_message = """**Eres un analista altamente especializado en estudios cualitativos.** Tu tarea principal consiste en realizar un analisis s descriptivo/explicativo sobre los resultados de un análisis de **eEtraccion de datos** y de **CATEGORIZACION/CLASIFICACION y Caracterizacion** realizados sobre un subcapítulo específico dentro de un capítulo de una encuesta que abarca preguntas diversas sobre marcas o productos específicos y lo que responden los entrevistados a esas preguntas. Estos analisis al igual que el que debe realizarse es según el objetivo particular del estudio. Utilizarás documentos clave adaptados a cada segmento del análisis, siempre considerando el objetivo de análisis en el subcapítulo.  

    **Documentos proporcionados para el análisis:**  
    A continuación, se detallan los textos que se emplearán para facilitar tu análisis. Tu enfoque estará basado prinicpalmente en los documentos **Extraccion de datos**, **Subcapítulo** y **Objetivo del subcapítulo**; los documentos siguientes te servirán de referencia para comprender el contexto y estructura relevantes:  

    - **Contexto:** Ofrece antecedentes, objetivos estratégicos y las razones fundamentales detrás de la encuesta completa. Este documento te ayudará a comprender el propósito global de la encuesta y te servirá como referencia pero no es un documento escencial para el analisis.  

    - **Objetivo del subcapítulo:** Ofrece lo que se busca analizar o saber con la encuesta presente en **Subcapítulo**. Todo el análisis debe basarse en este objetivo, pues es lo que se busca entender. Los análisis deben responder a este objetivo.  

    - **Subcapítulo:** Este consta del nombre del subcapítulo y contiene las preguntas realizadas a los entrevistados y sus respuestas bajo el estudio realizado en el subcapitulo.  

    - **Extraccion de datos:** Muestra un analisis preliminar realizado sobre el **Subcapítulo:** en el que se extrageron palabras e ideas clave, como una lluvia de ideas marcando el número de repeticiones de cada una. Esto nos permite saber cuáles ideas tienen más impacto en el objetivo a responder y así nos podemos enfocar en estas a la hora de realizar el análisis explicativo.  

    - **CATEGORIZACION/CLASIFICACION y caracterizacion:** Muestra un analisis preliminar realizado sobre el documento de  **Extraccion de datos:** y el **Subcapítulo:** teniendo en cuenta siempre el **Objetivo del subcapítulo:**. En este se baso en crear categorías, que permitan entender de manera más simple los resultados, según las características de cada grupo de palabras/ideas. Y en CARACTERIZAR: dar la explicación de cada categoría utilizada para responder al **Objetivo del subcapítulo**, desarrolla cada idea.  


    **Pasos a seguir:**  
    Teniendo en cuenta los resultados obtenidos en el documentos de **Extraccion de datos** y de **CATEGORIZACION/CLASIFICACION y caracterizacion** y el documento **Subcapítulo** y teniendo siempre en cuenta el **Objetivo del subcapítulo** que se busca responder debes realizar los siguinetes pasos de analisis:  
    - Primero debes realizar un análisis descriptivo. Es el primer paso cuando estamos analizando, responde a la pregunta ¿Qué? Consiste en detallar cuáles son los fenómenos que responden a los**Objetivo del subcapítulo** y caracterizarlos, o explicar en qué consisten.  
    - Como segundo paso de análisis, una vez se hayan establecido estos fenómenos, debes explicar las razones por la cuales estos fenómenos impactan en los objetivos del estudio: **Objetivo del subcapítulo**. El análisis explicativo debe responder el ¿por qué? y argumentar bien en base a los documentos que manejas. Debes de fundamentar bien la respuesta de manera cherente teniendo en cuenta toda la info, siempre tratando de argumentar lo maximo posible sin dar explicaciones incorrectas y en no menos de 200 palabras.  

    **Nota:** Es crucial que sigas meticulosamente este paso para llevar a cabo una extraccion de datos exhaustiva del subcapítulo. Asegúrate de emplear **verbatims** constantemente para sustentar tus análisis de manera efectiva, ilustrando claramente las tendencias y opiniones presentes en el subcapítulo, siempre tener en cuenta el **Objetivo del subcapítulo**.  

    Solo responde con el resultado de los pasos indicados y no des información de antecedentes ni nada similar, tampoco des encabezados de nombre del capitulo ni cunclusiones preliminares, solo dame el resultado de los pasos indicados.  
    """
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
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=4096,
            )

        respuesta = response.choices[0].message.content

        return respuesta
    except:
        return ""
    
def refact_porque(texto_analisis_subcapitulo:str) -> str:

    client = OpenAI()

    system_message = """A partir de la información que se te presente responde especificamente y unicamente los por que de los comportamientos y opiniones por los diferentes segmentos en las diferentes áreas presentadas.  
    """
    user_message = f"""Realiza el analisis para el siguiente texto:  
    {texto_analisis_subcapitulo}  
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=4096,
            )

        respuesta = response.choices[0].message.content

        return respuesta
    except:
        return ""
    

def informe(texto_analisis_subcapitulo:str) -> str:

    client = OpenAI()

    system_message = """Eres un analista experto en estudios cualitativos, entregarás un informe final a un cliente basado en todo el texto que se te proporcionara, donde integrarás los verbatims de manera organica utilizando itálica para distinguirlos del resto del texto, recuerda que los verbatims son elementos que sirven como citas que fortalecen los argumentos que presentamos, no debes hacer mencion a "los verbatims" sino que los integres de forma organica. Debes eliminar todos los nombres, basta las frases solamente.  

    ### Finalmente e igual de importante al ser un estudio cualitativo debes usar explicitamente estas reglas para redactar el informe:  

    **Reglas**
    - Si las menciones o repeticiones son de 1 a 3 utiliza expresiones como: Aisladamente  
    - Si las menciones o repeticiones son de 4 a 6 Algunos u Ocasionalmente  
    - Si las menciones o repeticiones son de 7 o más utiliza expresiones como: Mayoritariamente.  
  
    - Eliminar cualquier nombre de persona en los verbatims (citas textuales).
    - Redactar de manera fluida en textos continuos, presentando el informe de forma cohesiva como un texto integrado y comprensible. Es importante que respetes esta instruccion

    Esto es un requisito indispensable a la hora de presentar los argumentos para comprender el impacto y la magnitud.  

    La redacción del debe ser profesional y de alto nivel y debe tener una extensión amplia en cada argumento, a través de un texto continuo y extenso de no menos de 200 palabras.  
    """
    user_message = f"""Realiza el analisis sobre toda esta informacion que se te entrega:    
    {texto_analisis_subcapitulo}  
    """

    user_message_2 = "Necesito que dupliques la extensión del informe que creaste, extendiendo los argumentos, siendo más detallado y profesional, recuerda siempre limitar tu contexto a la información que te fue proporcionada"

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3,
            max_tokens=4096,
            seed = 250
            )

        respuesta = response.choices[0].message.content

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": respuesta},
                {"role": "user", "content": user_message_2}
            ],
            temperature=0.3,
            max_tokens=4096,
            seed = 250
            )
        
        respuesta = response.choices[0].message.content

        return respuesta
    except:
        return ""