from typing import TypedDict, List
from .read_dcument_util import (
    get_data_excel, 
    pdf_to_text
)

from .model_llm_utils import (
    extraccion_datos, 
    categorizar_clasificar, 
    analisis_1, 
    refact_porque, 
    informe
)

class SubCapitulo(TypedDict):
    """
    Estructura de un subcapítulo.

    Atributos:
    - nombre_subcapitulo (str): El nombre del subcapítulo.
    - extraccion_datos (str): Datos extraídos relacionados con el subcapítulo.
    - categorizar_clasificar (str): Categorías y caracterización del subcapítulo.
    - analisis (str): Análisis descriptivo del subcapítulo.
    - por_que (str): Razones y explicaciones detrás de los hallazgos.
    - informe (str): Informe final que resume los hallazgos del subcapítulo.
    """
    nombre_subcapitulo: str
    extraccion_datos: str
    categorizar_clasificar: str
    analisis: str
    por_que: str
    informe: str

class Capitulo(TypedDict):
    """
    Estructura de un capítulo.

    Atributos:
    - nombre_capitulo (str): El nombre del capítulo.
    - sub_capitulos (List[SubCapitulo]): Una lista de subcapítulos incluidos en este capítulo.
    """
    nombre_capitulo: str
    sub_capitulos: List[SubCapitulo]

# La salida de analisis general
SalidaFuncion = List[Capitulo]


def analisis_general(url_excel:str, 
                     url_pdf_esquema:str, 
                     url_pdf_context:str
)->SalidaFuncion:
    
    print(f"\n{'='*20}")
    print("Iniciando analisis general...")
    print("="*20)
    
    """
    Esta función genera una lista de capítulos, cada uno con sus respectivos subcapítulos,
    incluyendo análisis, categorías y datos extraídos.

    Returns:
        List[Capitulo]: Una lista de capítulos, donde cada capítulo contiene una lista
                        de subcapítulos con información detallada.

    Ejemplo de salida:
    [
        {
            'nombre_capitulo': 'EXPLORACIÓN GENERAL DE LA CATEGORÍA',
            'sub_capitulos': [
                {
                    'nombre_subcapitulo': 'ASOCIACIONES ESPONTÁNEAS',
                    'extraccion_datos': '### Extracción de Datos...',
                    'categorizar_clasificar': '### Categorías y Caracterización...',
                    'analisis': '### Análisis Descriptivo...',
                    'por_que': '### Análisis Explicativo...',
                    'informe': '### Informe Final:...'
                }
                # Más subcapítulos...
            ]
        }
        # Más capítulos...
    ]
    """
    
    # obtener datos de las url -------------------------------------------------------------------------------------
    list_cap = get_data_excel(url_excel)
    print(f"\n{'='*20}")
    print("Datos de la excel obtenidos correctamente")
    print("="*20)

    texto_contexto = pdf_to_text(url_pdf_context)
    print(f"\n{'='*20}")
    print("Datos del contexto obtenidos correctamente")
    print("="*20)


    texto_extructura = pdf_to_text(url_pdf_esquema)
    print(f"\n{'='*20}")
    print("Datos de la estructura obtenidos correctamente")
    print("="*20)

    # obtener los datos personales de los encuestados-----------------------------------------------------------------
    cap = 0
    nombre_capitulo = list_cap[cap][0]
    
    datos_personales = ""

    for sub_cap in list_cap[cap][1]:
        texto_objetivo = sub_cap[0]
        datos_personales += f"#### {sub_cap[1]}\n{sub_cap[2]}\n  "

    lista_analisis_capitulos = []

    # pasos del analisis por capitulo ---------------------------------------------------------------------------------
    for cap in range(1,len(list_cap)):
        
        sub_capitulos = []
        
        for sub_cap in list_cap[cap][1]:

            texto_objetivo = sub_cap[0] # obtengo el texto del objetivo del subcapitulo
            
            texto_subcapitulo = f"### Sub-Capitulo: {sub_cap[1]}\n{sub_cap[2]}" # obtengo el texto del sub capitulo

            # pasos del analisis ------------------
            
            texto_extraccion_datos = extraccion_datos(texto_contexto, 
                                                      texto_objetivo, 
                                                      texto_subcapitulo
                                                    )
            
            texto_categorizar_clasificar = categorizar_clasificar(texto_contexto, 
                                                                  texto_objetivo, 
                                                                  texto_subcapitulo, 
                                                                  texto_extraccion_datos, 
                                                                  datos_personales
                                                                )
        
            texto_analisis = analisis_1(texto_contexto, 
                                        texto_objetivo, 
                                        texto_subcapitulo, 
                                        texto_extraccion_datos, 
                                        texto_categorizar_clasificar
                                    )

            texto_analisis_subcapitulo = f"### Sub-Capitulo: {sub_cap[1]}" + texto_extraccion_datos + "\n\n" + texto_categorizar_clasificar + "\n\n" + texto_analisis + '\n\n'

            text_refact_porque = refact_porque(texto_analisis_subcapitulo)

            texto_analisis_subcapitulo += text_refact_porque

            informe_sub_1, informe_sub_2 = informe(texto_analisis_subcapitulo)

            dic_sub_capitulo = {'nombre_subcapitulo': sub_cap[1], 
                                'extraccion_datos': texto_extraccion_datos, 
                                'categorizar_clasificar':texto_categorizar_clasificar, 
                                'analisis': texto_analisis, 
                                'por_que':text_refact_porque, 
                                'informe_preliminar':informe_sub_1, 
                                'informe':informe_sub_2
                            }

            sub_capitulos.append(dic_sub_capitulo)

            #break

        nombre_capitulo = list_cap[cap][0] # obtengo el nombre del capitulo

        dic_analisis_cap = {'nombre_capitulo': nombre_capitulo, 'sub_capitulos': sub_capitulos}

        lista_analisis_capitulos.append(dic_analisis_cap)

        #break

    return lista_analisis_capitulos
