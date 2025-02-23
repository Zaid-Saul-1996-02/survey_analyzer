
# Survey Analyzer  

Este proyecto tiene como objetivo analizar una encuesta y generar un informe con los resultados.
Ademas un chatbot para responder preguntas sobre una encuesta.
Fue desarrollado aplicando IA Generativa y IA RAG (Recuperación de información basada en el contenido) con OpenAI, Langchain, Langgraph, FastAPI y el motor de base de datos MongoDB. Para las partes de procesamiento de datos se utilizó la libreria de Pandas.
En la parte de la IA Generativa se aplico el modelo GPT-4o y GPT-4o-mini.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:  

- **`app/main.py`**: Punto de entrada de la aplicación FastAPI.
- **`app/core/dependencies.py`**: Contiene las dependencias comunes, como la validación de la API key (`get_api_key`).
- **`app/schemas/shema.py`**: Define los esquemas Pydantic para la validación de datos, como `RequestDataLk`.
- **`app/services/agent/agent.py`**: Contiene la lógica de negocio para generar el plan de acción (`agent`).
- **`app/services/analisis/analisis_general.py`**: Contiene la lógica de negocio para generar el plan de acción (`analisis_general`).
- **`app/routers/`**: Contiene los routers de la API, como el router para el endpoint `/analizar` y `/bot`.

## Instalación

Para ejecutar el proyecto, se requiere:
- Python 3.12, recomendado: (3.12.8)
- Api Key para OpenAI.

Variables de entorno:  

- `OPENAI_API_KEY`: Clave de API para OpenAI.  
- `API_KEY_AUTH`: Clave de API para la autenticación.  
- `URI_MONGO`: URI de la base de datos MongoDB.
- `NAME_DB_MONGO`: Nombre de la base de datos MongoDB.
- `NAME_VECTOR_COLLECTION_DB_MONGO`: Nombre de la colección MongoDB para los vectores.
- `NAME_STATE_COLLECTION_DB_MONGO`: Nombre de la colección MongoDB para el estado de la conversación.

Se recomienda usar un entorno virtual para instalar las dependencias:

```bash (Linux/MacOS)
python -m venv nombre-del-entorno
source nombre-del-entorno/bin/activate
```

```bash (Windows)
python -m venv nombre-del-entorno
nombre-del-entorno\Scripts\activate
```

1. **Clona el repositorio:**

```bash
git clone https://github.com/edistone/survey_analyzer.git
cd survey_analyzer
```

2. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

3. **Ejecuta la aplicación:**

De esta manera se ejecuta la aplicación en modo de desarrollo y se reinicia automáticamente al guardar cambios:  

```bash
fastapi dev main.py
```

```bash
uvicorn app.main:app --reload
```

O de esta manera se ejecuta la aplicación en modo de producción:

```bash
uvicorn app.main:app
```

La API estará disponible en `http://127.0.0.1:8000`.

## Documentación de la API

La API sigue el estándar OpenAPI 3.1, y la documentación completa se puede encontrar en `http://127.0.0.1:8000/docs`.

## Endpoints

### 1. Analizar

**URL**: `/analizar`

**Método**: `POST`

**Puerto**: 8000

**Headers**:
- `Content-Type: application/json`
- `api-key-auth: *****`

**Body**:
```json
{   "url_excel": "https://sample.edistone.net/files/Project/Agent/2839%20-%20Pre%20Analisis-V2.xlsx",
    "url_pdf_esquema": "https://sample.edistone.net/files/Project/Agent/2839-Esquema%20Informe.pdf",
    "url_pdf_context": "https://sample.edistone.net/files/Project/Agent/2839-Contexto.pdf"
}
```

**Comando CURL**:
```sh
curl -X POST http://127.0.0.1:8000/analizar \
    -H "Content-Type: application/json" \
    -H "api-key-auth: *****" \
    -d '{   "url_excel": "https://sample.edistone.net/files/Project/Agent/2839%20-%20Pre%20Analisis-V2.xlsx",
    "url_pdf_esquema": "https://sample.edistone.net/files/Project/Agent/2839-Esquema%20Informe.pdf",
    "url_pdf_context": "https://sample.edistone.net/files/Project/Agent/2839-Contexto.pdf"
}'
```

**Salida:**
```json
{
    "data": [
        {
            "nombre_capitulo": "EXPLORACIÓN GENERAL DE LA CATEGORÍA",
            "sub_capitulos": [
                {
                    "nombre_subcapitulo": "ASOCIACIONES ESPONTÁNEAS",
                    "extraccion_datos": "**Extracción de datos del subcapítulo:**\n\n### Palabras e ideas clave (PRODUCTOS DE RIESGO REDUCIDO):\n- IQOS (6)\n- Salud/Saludable (5)\n- Comodidad (2)\n- Alternativa (1)\n- Seguridad (1)\n- Confiable (1)\n- Inocuidad (1)\n- Menor riesgo (1)\n- Innovación (1)\n- Medio ambiente (2)\n- Reducción de costos (1)\n- Responsabilidad (1)\n- Peligro (1)\n- Vapor (1)\n- Precaución (2)\n- Naturaleza (2)\n- Sostenibilidad (1)\n- Aire libre (1)\n- Productos naturales (1)\n- Patineta (1)\n- Bicicleta (1)\n- Carros híbridos (1)\n- Orgánico (1)\n- Agua (1)\n- Cerveza natural (1)\n- Termino medio (1)\n- Apto para todo (1)\n- Condón (1)\n- Precaución (1)\n- Alternativas (1)\n- Contaminación ambiental (1)\n- Impacto reducido (1)\n- Innovación (1)\n- Avance (1)\n- Desarrollo (1)\n- Estudio (1)\n- Bienestar (1)\n- Seguridad (1)\n- Reducción de costos (1)\n- Responsabilidad (1)\n- Químicos (1)\n- Peligro (1)\n- Vapor (1)\n\n### Palabras e ideas clave (TABACO SIN COMBUSTIÓN):\n- IQOS (10)\n- Vapeador (4)\n- Sin alquitrán (2)\n- Sin olor (3)\n- Diferente (1)\n- Ecosistema (1)\n- Contaminación (1)\n- Polvo (1)\n- Novedoso (2)\n- Evaporado (1)\n- Tabaco más limpio (1)\n- Sin calentarse (1)\n- Sin filtro (1)\n- Cero olor (1)\n- Sin cenizas (2)\n- Cultura (1)\n- Modernización (1)\n- Menos humo (1)\n- Menos sustancias dañinas (1)\n- Sin fuego (1)\n- Menos contaminación (1)\n- Practicidad (1)\n- Comodidad (1)\n- Habanos (1)\n- Heets (1)\n- Amber (1)\n- Siena (1)\n- Menos nocivo (1)\n- Nuevo sabor (1)\n- Humo limpio (1)\n- Cero nicotina (1)\n- Bienestar (1)\n- Vapor (1)\n- Menos dañino (1)\n\n### Repeticiones y asociaciones más destacadas:\n- **IQOS**: 16 menciones en total (6 en \"Productos de riesgo reducido\" y 10 en \"Tabaco sin combustión\").\n- **Salud/Saludable**: 5 menciones en \"Productos de riesgo reducido\".\n- **Vapeador**: 4 menciones en \"Tabaco sin combustión\".\n- **Sin olor**: 3 menciones en \"Tabaco sin combustión\".\n- **Novedoso**: 2 menciones en \"Tabaco sin combustión\".\n- **Sin alquitrán**: 2 menciones en \"Tabaco sin combustión\".\n- **Sin cenizas**: 2 menciones en \"Tabaco sin combustión\".\n- **Comodidad**: 2 menciones en \"Productos de riesgo reducido\" y 1 en \"Tabaco sin combustión\".\n- **Precaución**: 2 menciones en \"Productos de riesgo reducido\".\n- **Naturaleza**: 2 menciones en \"Productos de riesgo reducido\".\n- **Medio ambiente**: 2 menciones en \"Productos de riesgo reducido\".\n\n### Verbatims destacados:\n- \"IQOS, saludable, seguridad, saludable, salud, reducción de costos.\"\n- \"Vapeador, piensas en el IQOS automáticamente.\"\n- \"IQOS, sin alquitrán, sin olor.\"\n- \"Menos humo, menos olor, menos sustancias dañinas.\"\n- \"IQOS, habanos, heets, amber, siena, menos nocivo, nuevo sabor.\"\n- \"IQOS, humo limpio, salud, cero nicotina, novedoso, bienestar.\"\n\n### Conclusión preliminar:\nLas asociaciones más fuertes hacia \"Productos de riesgo reducido\" y \"Tabaco sin combustión\" están claramente vinculadas a IQOS, salud, y la reducción de riesgos y daños. La percepción de innovación y modernización también es notable, especialmente en el contexto de \"Tabaco sin combustión\".",
                    "categorizar_clasificar": "### Categorías y Caracterización\n\n#### Categorías:\n\n1. **IQOS y Productos Relacionados**\n2. **Salud y Bienestar**\n3. **Innovación y Modernización**\n4. **Medio Ambiente y Sostenibilidad**\n5. **Comodidad y Practicidad**\n6. **Seguridad y Reducción de Riesgos**\n7. **Percepciones Negativas**\n\n#### Caracterización:\n\n1. **IQOS y Productos Relacionados:**\n   - **Descripción:** Esta categoría agrupa todas las menciones directas a IQOS y productos relacionados como vapeadores y heets.\n   - **Verbatims:** \"IQOS, saludable, seguridad, saludable, salud, reducción de costos.\", \"Vapeador, piensas en el IQOS automáticamente.\"\n   - **Segmentos:** La mención de IQOS es transversal a todos los segmentos de edad y ocupación, indicando una fuerte asociación de la marca con los conceptos evaluados.\n\n2. **Salud y Bienestar:**\n   - **Descripción:** Incluye menciones a salud, saludable, bienestar y reducción de sustancias dañinas.\n   - **Verbatims:** \"Salud, comodidad, alternativas, inocuidad, menor riesgo.\", \"Menos humo, menos olor, menos sustancias dañinas.\"\n   - **Segmentos:** Predominante en adultos jóvenes (20-35 años) y profesionales de la salud, quienes valoran la reducción de riesgos y el bienestar.\n\n3. **Innovación y Modernización:**\n   - **Descripción:** Agrupa términos como novedoso, avance, desarrollo, y modernización.\n   - **Verbatims:** \"Innovación, avance, desarrollo, estudio.\", \"IQOS, humo limpio, salud, cero nicotina, novedoso, bienestar.\"\n   - **Segmentos:** Común en profesionales y estudiantes, quienes asocian estos productos con tecnología avanzada y modernidad.\n\n4. **Medio Ambiente y Sostenibilidad:**\n   - **Descripción:** Incluye menciones a medio ambiente, sostenibilidad, naturaleza, y reducción de contaminación.\n   - **Verbatims:** \"Contaminación ambiental, impacto reducido, medio ambiente.\", \"Sin alquitrán, sin olor, menos contaminación.\"\n   - **Segmentos:** Más frecuente en personas con ocupaciones relacionadas con la administración pública y la educación, quienes muestran una mayor conciencia ambiental.\n\n5. **Comodidad y Practicidad:**\n   - **Descripción:** Agrupa menciones a comodidad, practicidad, y conveniencia.\n   - **Verbatims:** \"Comodidad, alternativas, practicidad.\", \"Menos cenizas, sin fuego, comodidad.\"\n   - **Segmentos:** Común en adultos jóvenes y personas con estilos de vida activos, quienes valoran la conveniencia y facilidad de uso.\n\n6. **Seguridad y Reducción de Riesgos:**\n   - **Descripción:** Incluye menciones a seguridad, confiabilidad, y menor riesgo.\n   - **Verbatims:** \"Seguridad, confiable, inocuidad, menor riesgo.\", \"IQOS, sin fuego, menos nocivo.\"\n   - **Segmentos:** Predominante en personas mayores (35-50 años) y profesionales de la salud, quienes priorizan la seguridad y la reducción de riesgos.\n\n7. **Percepciones Negativas:**\n   - **Descripción:** Agrupa menciones a peligro y precaución.\n   - **Verbatims:** \"Peligro, precaución.\", \"Condón, precaución.\"\n   - **Segmentos:** Menos frecuente, pero presente en algunos adultos mayores y personas con ocupaciones relacionadas con la seguridad y la salud.\n\n### Diferencias entre Segmentos:\n\n- **Edad:** Los adultos jóvenes (20-35 años) tienden a asociar más los productos con innovación, modernización, y comodidad. Los adultos mayores (35-50 años) se enfocan más en la seguridad y la reducción de riesgos.\n- **Ocupación:** Los profesionales de la salud y la educación muestran una mayor preocupación por la salud y el medio ambiente. Los estudiantes y profesionales en tecnología y administración valoran más la innovación y la modernización.\n- **Estilo de Vida:** Las personas con estilos de vida activos y ocupados valoran la comodidad y practicidad de los productos, mientras que aquellos con una mayor conciencia ambiental se enfocan en la sostenibilidad y la reducción de la contaminación.\n\n### Conclusión:\n\nLas asociaciones hacia \"Productos de riesgo reducido\" y \"Tabaco sin combustión\" están fuertemente vinculadas a IQOS, salud, y la reducción de riesgos y daños. La percepción de innovación y modernización es notable, especialmente en el contexto de \"Tabaco sin combustión\". Las diferencias entre segmentos indican que las estrategias de marketing deben ser personalizadas según la edad, ocupación, y estilo de vida de los consumidores.",
                    "analisis": "### Análisis Descriptivo\n\n**¿Qué?**\n\nLos fenómenos identificados en el subcapítulo relacionado con \"Productos de riesgo reducido\" y \"Tabaco sin combustión\" se pueden agrupar en varias categorías clave, según las asociaciones espontáneas de los entrevistados:\n\n1. **IQOS y Productos Relacionados**: La marca IQOS es mencionada de manera recurrente en ambos conceptos, con 6 menciones en \"Productos de riesgo reducido\" y 10 en \"Tabaco sin combustión\". Ejemplos de verbatims incluyen: \"IQOS, saludable, seguridad, saludable, salud, reducción de costos.\" y \"Vapeador, piensas en el IQOS automáticamente.\"\n\n2. **Salud y Bienestar**: Las asociaciones hacia la salud y el bienestar son prominentes, con 5 menciones en \"Productos de riesgo reducido\". Verbatims relevantes incluyen: \"Salud, comodidad, alternativas, inocuidad, menor riesgo.\"\n\n3. **Innovación y Modernización**: Términos como novedoso, avance, y desarrollo son comunes, especialmente en \"Tabaco sin combustión\". Ejemplos de verbatims son: \"Innovación, avance, desarrollo, estudio.\" y \"IQOS, humo limpio, salud, cero nicotina, novedoso, bienestar.\"\n\n4. **Medio Ambiente y Sostenibilidad**: Los entrevistados mencionaron términos relacionados con la sostenibilidad y el impacto ambiental, tales como \"medio ambiente\", \"sostenibilidad\", y \"reducción de contaminación\". Verbatims incluyen: \"Contaminación ambiental, impacto reducido, medio ambiente.\"\n\n5. **Comodidad y Practicidad**: Esta categoría engloba menciones a la comodidad y practicidad del uso de estos productos. Ejemplos: \"Comodidad, alternativas, practicidad.\" y \"Menos cenizas, sin fuego, comodidad.\"\n\n6. **Seguridad y Reducción de Riesgos**: Los entrevistados asocian estos productos con seguridad y menor riesgo. Verbatims relevantes: \"Seguridad, confiable, inocuidad, menor riesgo.\" y \"IQOS, sin fuego, menos nocivo.\"\n\n7. **Percepciones Negativas**: Aunque menos frecuente, existe cierta percepción negativa, incluyendo términos como peligro y precaución. Ejemplos de verbatims: \"Peligro, precaución.\" y \"Condón, precaución.\"\n\n### Análisis Explicativo\n\n**¿Por qué?**\n\nLas asociaciones identificadas tienen un impacto significativo en el objetivo del subcapítulo: **\"Identificar las asociaciones que tiene el consumidor de la categoría hacia los conceptos de 'Productos de riesgo reducido' y 'Tabaco sin combustión'.\"** \n\n1. **IQOS y Productos Relacionados**: La fuerte presencia de IQOS en las respuestas indica una alta notoriedad de la marca en la mente de los consumidores cuando piensan en productos de riesgo reducido y tabaco sin combustión. Esta asociación sugiere que IQOS está efectivamente posicionado como líder en esta categoría, lo cual es crucial para cualquier estrategia de marketing y comunicación dirigida a resaltar estos atributos. La repetición frecuente del término \"IQOS\" (16 menciones en total) subraya su dominancia en el mercado y su reconocimiento como un producto innovador y seguro.\n\n2. **Salud y Bienestar**: Las asociaciones con salud y bienestar reflejan la percepción de los consumidores de que estos productos son menos dañinos que los cigarrillos tradicionales. Esto es vital para el objetivo del subcapítulo, ya que resaltar los beneficios para la salud puede ser un punto de venta crucial. Los verbatims como \"Salud, comodidad, alternativas, inocuidad, menor riesgo.\" indican que los consumidores perciben estos productos como opciones más seguras y saludables, lo cual puede influir significativamente en su decisión de compra.\n\n3. **Innovación y Modernización**: La percepción de innovación y modernización es un aspecto importante que distingue a estos productos de los cigarrillos tradicionales. Los consumidores asocian términos como \"novedoso\" y \"modernización\" con estos productos, lo que sugiere que ven a IQOS y productos similares como avances tecnológicos en la industria del tabaco. La innovación puede ser un factor de atracción para consumidores jóvenes y tecnológicamente orientados, fortaleciendo la posición de la marca en segmentos específicos.\n\n4. **Medio Ambiente y Sostenibilidad**: Las menciones a la sostenibilidad y el impacto ambiental indican una creciente preocupación por estos temas entre los consumidores. Asociaciones como \"Contaminación ambiental, impacto reducido, medio ambiente.\" sugieren que los consumidores valoran los productos que son percibidos como más sostenibles. Esto puede ser aprovechado en campañas de marketing que destaquen los beneficios ambientales de los productos IQOS.\n\n5. **Comodidad y Practicidad**: La comodidad y practicidad son factores importantes que pueden influir en la adopción de estos productos. Los verbatims como \"Comodidad, alternativas, practicidad.\" indican que los consumidores aprecian la facilidad de uso y la conveniencia que estos productos ofrecen, lo cual puede ser un diferenciador clave en el mercado.\n\n6. **Seguridad y Reducción de Riesgos**: La percepción de seguridad y reducción de riesgos es fundamental para convencer a los consumidores de cambiar a estos productos. Verbatims como \"Seguridad, confiable, inocuidad, menor riesgo.\" refuerzan la idea de que estos productos son vistos como opciones más seguras, lo cual es un punto crucial para atraer a consumidores preocupados por los riesgos asociados al consumo de tabaco.\n\n7. **Percepciones Negativas**: Aunque menos frecuentes, las percepciones negativas como \"Peligro, precaución.\" indican que todavía existen barreras y preocupaciones que deben ser abordadas en la comunicación y educación sobre estos productos. Es importante que las campañas de marketing también se enfoquen en mitigar estas percepciones negativas para mejorar la aceptación general.\n\nEn conclusión, las asociaciones identificadas proporcionan una visión clara de cómo los consumidores perciben los \"Productos de riesgo reducido\" y el \"Tabaco sin combustión\". Estas asociaciones no solo ayudan a entender la percepción actual de los consumidores, sino que también ofrecen direcciones estratégicas para futuras campañas de marketing y posicionamiento de la marca.",
                    "por_que": "### ¿Por qué?\n\n#### IQOS y Productos Relacionados:\n**IQOS** es una marca que ha logrado una alta notoriedad en la mente de los consumidores, especialmente cuando piensan en productos de riesgo reducido y tabaco sin combustión. Esta fuerte presencia se debe a la estrategia de marketing efectiva de IQOS, que ha enfatizado tanto la innovación como la reducción de daños en comparación con los cigarrillos tradicionales. El reconocimiento de la marca sugiere que IQOS se ha posicionado como líder en este nicho de mercado, lo cual es crucial para mantener y expandir su base de consumidores.\n\n#### Salud y Bienestar:\nLa asociación con **salud y bienestar** refleja la percepción de que estos productos son menos dañinos que los cigarrillos convencionales. Esta percepción se debe a la comunicación efectiva de los beneficios para la salud que estos productos ofrecen, tales como la ausencia de alquitrán y la reducción de sustancias nocivas. Los consumidores, especialmente aquellos preocupados por su salud, encuentran en estos productos una alternativa que les permite continuar con su hábito de fumar pero con un menor riesgo para su salud.\n\n#### Innovación y Modernización:\nLos términos como **novedoso** y **modernización** indican que los consumidores ven a estos productos como avances tecnológicos significativos en la industria del tabaco. Esta percepción se debe a las características innovadoras de los productos, como la tecnología de calentamiento sin combustión y la disponibilidad de sabores variados. Los consumidores jóvenes y tecnológicamente orientados son especialmente atraídos por estos aspectos, ya que buscan productos que se alineen con su estilo de vida moderno y avanzado.\n\n#### Medio Ambiente y Sostenibilidad:\nLa preocupación por el **medio ambiente y la sostenibilidad** es cada vez más prominente entre los consumidores. Las menciones a la reducción de la contaminación y el impacto ambiental se deben a la percepción de que estos productos generan menos residuos y contaminación en comparación con los cigarrillos tradicionales. Esto es especialmente relevante para consumidores con una mayor conciencia ambiental, quienes valoran los productos que minimizan su impacto negativo en el entorno.\n\n#### Comodidad y Practicidad:\nLa **comodidad y practicidad** son factores importantes que influyen en la adopción de estos productos. Los consumidores valoran la facilidad de uso y la conveniencia, como la ausencia de cenizas y el menor olor. Estas características hacen que los productos sean más atractivos para personas con estilos de vida activos y ocupados, quienes buscan soluciones que se adapten a su ritmo de vida.\n\n#### Seguridad y Reducción de Riesgos:\nLa percepción de **seguridad y reducción de riesgos** es fundamental para atraer a nuevos usuarios. Los consumidores, especialmente los mayores y los profesionales de la salud, priorizan productos que ofrecen un menor riesgo en comparación con los cigarrillos convencionales. Las características como la ausencia de fuego y la reducción de sustancias nocivas refuerzan esta percepción, haciendo que estos productos sean vistos como opciones más seguras.\n\n#### Percepciones Negativas:\nAunque menos frecuentes, las menciones a **peligro y precaución** indican que aún existen preocupaciones y barreras que deben ser abordadas. Estas percepciones negativas pueden estar basadas en la falta de información o en experiencias previas con productos de tabaco. Es crucial que las campañas de marketing y educación se enfoquen en mitigar estas preocupaciones, proporcionando información clara y basada en evidencia sobre los beneficios y la seguridad de estos productos.\n\n### Diferencias entre Segmentos:\n\n#### Edad:\n- **Adultos jóvenes (20-35 años)**: Asocian más los productos con innovación, modernización, y comodidad porque buscan productos que se alineen con sus estilos de vida activos y tecnológicamente avanzados.\n- **Adultos mayores (35-50 años)**: Se enfocan más en la seguridad y la reducción de riesgos debido a mayores preocupaciones por su salud y bienestar a largo plazo.\n\n#### Ocupación:\n- **Profesionales de la salud y la educación**: Muestran una mayor preocupación por la salud y el medio ambiente debido a su formación y conciencia profesional.\n- **Estudiantes y profesionales en tecnología y administración**: Valoran más la innovación y la modernización porque están inmersos en entornos que priorizan el avance tecnológico y la eficiencia.\n\n#### Estilo de Vida:\n- **Estilos de vida activos y ocupados**: Valoran la comodidad y practicidad de los productos porque necesitan soluciones que se adapten a su ritmo de vida.\n- **Conciencia ambiental**: Se enfocan en la sostenibilidad y la reducción de la contaminación porque buscan minimizar su impacto negativo en el medio ambiente.\n\n### Conclusión:\nLas asociaciones identificadas permiten entender cómo los consumidores perciben los \"Productos de riesgo reducido\" y el \"Tabaco sin combustión\". IQOS ha logrado posicionarse efectivamente en la mente de los consumidores, asociándose con salud, innovación, y reducción de riesgos. Las diferencias entre segmentos indican que las estrategias de marketing deben ser personalizadas según la edad, ocupación, y estilo de vida de los consumidores para maximizar su efectividad.",
                    "informe": "### Informe Final: Análisis de Asociaciones Espontáneas en Productos de Riesgo Reducido y Tabaco sin Combustión\n\n**Sub-Capítulo: ASOCIACIONES ESPONTÁNEAS**\n\n#### Introducción\n\nEl presente informe tiene como objetivo analizar las asociaciones espontáneas de los consumidores hacia los conceptos de \"Productos de riesgo reducido\" y \"Tabaco sin combustión\". Este análisis se basa en las menciones y repeticiones de palabras clave y verbatims extraídos de las respuestas de los entrevistados, proporcionando una visión integral de las percepciones y actitudes hacia estos productos. A través de un análisis detallado, se busca comprender cómo los consumidores perciben estos productos y qué factores influyen en su aceptación y uso.\n\n#### Categorías y Caracterización\n\n1. **IQOS y Productos Relacionados**\n   - **Descripción:** Esta categoría agrupa todas las menciones directas a IQOS y productos relacionados como vapeadores y heets. La marca IQOS ha logrado una fuerte presencia en la mente de los consumidores, siendo mencionada 16 veces en total, lo que indica una alta notoriedad y reconocimiento. Esta asociación no es casual, sino el resultado de una estrategia de marketing bien ejecutada que ha enfatizado tanto la innovación como la reducción de daños en comparación con los cigarrillos tradicionales.\n   - **Verbatims:** _\"IQOS, saludable, seguridad, saludable, salud, reducción de costos.\"_, _\"Vapeador, piensas en el IQOS automáticamente.\"_\n   - **Segmentos:** La mención de IQOS es transversal a todos los segmentos de edad y ocupación, indicando una fuerte asociación de la marca con los conceptos evaluados. Esto sugiere que IQOS ha logrado posicionarse como un referente en la categoría de productos de riesgo reducido y tabaco sin combustión, lo cual es crucial para mantener y expandir su base de consumidores.\n\n2. **Salud y Bienestar**\n   - **Descripción:** Incluye menciones a salud, saludable, bienestar y reducción de sustancias dañinas. Las asociaciones con salud y bienestar reflejan la percepción de los consumidores de que estos productos son menos dañinos que los cigarrillos tradicionales. Esta percepción es vital para el objetivo del subcapítulo, ya que resaltar los beneficios para la salud puede ser un punto de venta crucial.\n   - **Verbatims:** _\"Salud, comodidad, alternativas, inocuidad, menor riesgo.\"_, _\"Menos humo, menos olor, menos sustancias dañinas.\"_\n   - **Segmentos:** Predominante en adultos jóvenes (20-35 años) y profesionales de la salud, quienes valoran la reducción de riesgos y el bienestar. Estos segmentos encuentran en estos productos una alternativa que les permite continuar con su hábito de fumar pero con un menor riesgo para su salud, lo cual puede influir significativamente en su decisión de compra.\n\n3. **Innovación y Modernización**\n   - **Descripción:** Agrupa términos como novedoso, avance, desarrollo, y modernización. La percepción de innovación y modernización es un aspecto importante que distingue a estos productos de los cigarrillos tradicionales. Los consumidores asocian términos como _\"novedoso\"_ y _\"modernización\"_ con estos productos, lo que sugiere que ven a IQOS y productos similares como avances tecnológicos en la industria del tabaco.\n   - **Verbatims:** _\"Innovación, avance, desarrollo, estudio.\"_, _\"IQOS, humo limpio, salud, cero nicotina, novedoso, bienestar.\"_\n   - **Segmentos:** Común en profesionales y estudiantes, quienes asocian estos productos con tecnología avanzada y modernidad. La innovación puede ser un factor de atracción para consumidores jóvenes y tecnológicamente orientados, fortaleciendo la posición de la marca en segmentos específicos.\n\n4. **Medio Ambiente y Sostenibilidad**\n   - **Descripción:** Incluye menciones a medio ambiente, sostenibilidad, naturaleza, y reducción de contaminación. Las menciones a la sostenibilidad y el impacto ambiental indican una creciente preocupación por estos temas entre los consumidores. Asociaciones como _\"Contaminación ambiental, impacto reducido, medio ambiente.\"_ sugieren que los consumidores valoran los productos que son percibidos como más sostenibles.\n   - **Verbatims:** _\"Contaminación ambiental, impacto reducido, medio ambiente.\"_, _\"Sin alquitrán, sin olor, menos contaminación.\"_\n   - **Segmentos:** Más frecuente en personas con ocupaciones relacionadas con la administración pública y la educación, quienes muestran una mayor conciencia ambiental. Esto puede ser aprovechado en campañas de marketing que destaquen los beneficios ambientales de los productos IQOS, atrayendo a consumidores con una mayor conciencia ambiental.\n\n5. **Comodidad y Practicidad**\n   - **Descripción:** Agrupa menciones a comodidad, practicidad, y conveniencia. La comodidad y practicidad son factores importantes que pueden influir en la adopción de estos productos. Los verbatims como _\"Comodidad, alternativas, practicidad.\"_ indican que los consumidores aprecian la facilidad de uso y la conveniencia que estos productos ofrecen.\n   - **Verbatims:** _\"Comodidad, alternativas, practicidad.\"_, _\"Menos cenizas, sin fuego, comodidad.\"_\n   - **Segmentos:** Común en adultos jóvenes y personas con estilos de vida activos, quienes valoran la conveniencia y facilidad de uso. Estas características hacen que los productos sean más atractivos para personas con estilos de vida activos y ocupados, quienes buscan soluciones que se adapten a su ritmo de vida.\n\n6. **Seguridad y Reducción de Riesgos**\n   - **Descripción:** Incluye menciones a seguridad, confiabilidad, y menor riesgo. La percepción de seguridad y reducción de riesgos es fundamental para convencer a los consumidores de cambiar a estos productos. Verbatims como _\"Seguridad, confiable, inocuidad, menor riesgo.\"_ refuerzan la idea de que estos productos son vistos como opciones más seguras.\n   - **Verbatims:** _\"Seguridad, confiable, inocuidad, menor riesgo.\"_, _\"IQOS, sin fuego, menos nocivo.\"_\n   - **Segmentos:** Predominante en personas mayores (35-50 años) y profesionales de la salud, quienes priorizan la seguridad y la reducción de riesgos. Estos segmentos son especialmente importantes, ya que su adopción de estos productos puede influir en otros consumidores preocupados por los riesgos asociados al consumo de tabaco.\n\n7. **Percepciones Negativas**\n   - **Descripción:** Agrupa menciones a peligro y precaución. Aunque menos frecuente, existe cierta percepción negativa, incluyendo términos como peligro y precaución. Estas percepciones negativas pueden estar basadas en la falta de información o en experiencias previas con productos de tabaco.\n   - **Verbatims:** _\"Peligro, precaución.\"_, _\"Condón, precaución.\"_\n   - **Segmentos:** Menos frecuente, pero presente en algunos adultos mayores y personas con ocupaciones relacionadas con la seguridad y la salud. Es crucial que las campañas de marketing y educación se enfoquen en mitigar estas preocupaciones, proporcionando información clara y basada en evidencia sobre los beneficios y la seguridad de estos productos.\n\n#### Diferencias entre Segmentos\n\n- **Edad:** Los adultos jóvenes (20-35 años) tienden a asociar más los productos con innovación, modernización, y comodidad. Estos consumidores buscan productos que se alineen con sus estilos de vida activos y tecnológicamente avanzados. Por otro lado, los adultos mayores (35-50 años) se enfocan más en la seguridad y la reducción de riesgos debido a mayores preocupaciones por su salud y bienestar a largo plazo.\n- **Ocupación:** Los profesionales de la salud y la educación muestran una mayor preocupación por la salud y el medio ambiente debido a su formación y conciencia profesional. Estos segmentos valoran los productos que ofrecen beneficios para la salud y que son percibidos como más sostenibles. En contraste, los estudiantes y profesionales en tecnología y administración valoran más la innovación y la modernización porque están inmersos en entornos que priorizan el avance tecnológico y la eficiencia.\n- **Estilo de Vida:** Las personas con estilos de vida activos y ocupados valoran la comodidad y practicidad de los productos porque necesitan soluciones que se adapten a su ritmo de vida. Estos consumidores buscan productos que sean fáciles de usar y que no interfieran con sus actividades diarias. Por otro lado, aquellos con una mayor conciencia ambiental se enfocan en la sostenibilidad y la reducción de la contaminación porque buscan minimizar su impacto negativo en el medio ambiente.\n\n#### Análisis Descriptivo\n\n**¿Qué?**\n\nLos fenómenos identificados en el subcapítulo relacionado con \"Productos de riesgo reducido\" y \"Tabaco sin combustión\" se pueden agrupar en varias categorías clave, según las asociaciones espontáneas de los entrevistados:\n\n1. **IQOS y Productos Relacionados:** La marca IQOS es mencionada de manera recurrente en ambos conceptos, con 6 menciones en \"Productos de riesgo reducido\" y 10 en \"Tabaco sin combustión\". Ejemplos de verbatims incluyen: _\"IQOS, saludable, seguridad, saludable, salud, reducción de costos.\"_ y _\"Vapeador, piensas en el IQOS automáticamente.\"_\n\n2. **Salud y Bienestar:** Las asociaciones hacia la salud y el bienestar son prominentes, con 5 menciones en \"Productos de riesgo reducido\". Verbatims relevantes incluyen: _\"Salud, comodidad, alternativas, inocuidad, menor riesgo.\"_\n\n3. **Innovación y Modernización:** Términos como novedoso, avance, y desarrollo son comunes, especialmente en \"Tabaco sin combustión\". Ejemplos de verbatims son: _\"Innovación, avance, desarrollo, estudio.\"_ y _\"IQOS, humo limpio, salud, cero nicotina, novedoso, bienestar.\"_\n\n4. **Medio Ambiente y Sostenibilidad:** Los entrevistados mencionaron términos relacionados con la sostenibilidad y el impacto ambiental, tales como \"medio ambiente\", \"sostenibilidad\", y \"reducción de contaminación\". Verbatims incluyen: _\"Contaminación ambiental, impacto reducido, medio ambiente.\"_\n\n5. **Comodidad y Practicidad:** Esta categoría engloba menciones a la comodidad y practicidad del uso de estos productos. Ejemplos: _\"Comodidad, alternativas, practicidad.\"_ y _\"Menos cenizas, sin fuego, comodidad.\"_\n\n6. **Seguridad y Reducción de Riesgos:** Los entrevistados asocian estos productos con seguridad y menor riesgo. Verbatims relevantes: _\"Seguridad, confiable, inocuidad, menor riesgo.\"_ y _\"IQOS, sin fuego, menos nocivo.\"_\n\n7. **Percepciones Negativas:** Aunque menos frecuente, existe cierta percepción negativa, incluyendo términos como peligro y precaución. Ejemplos de verbatims: _\"Peligro, precaución.\"_ y _\"Condón, precaución.\"_\n\n#### Análisis Explicativo\n\n**¿Por qué?**\n\nLas asociaciones identificadas tienen un impacto significativo en el objetivo del subcapítulo: **\"Identificar las asociaciones que tiene el consumidor de la categoría hacia los conceptos de 'Productos de riesgo reducido' y 'Tabaco sin combustión'.\"**\n\n1. **IQOS y Productos Relacionados:** La fuerte presencia de IQOS en las respuestas indica una alta notoriedad de la marca en la mente de los consumidores cuando piensan en productos de riesgo reducido y tabaco sin combustión. Esta asociación sugiere que IQOS está efectivamente posicionado como líder en esta categoría, lo cual es crucial para cualquier estrategia de marketing y comunicación dirigida a resaltar estos atributos. La repetición frecuente del término \"IQOS\" (16 menciones en total) subraya su dominancia en el mercado y su reconocimiento como un producto innovador y seguro. Esta notoriedad no es casual, sino el resultado de una estrategia de marketing bien ejecutada que ha enfatizado tanto la innovación como la reducción de daños en comparación con los cigarrillos tradicionales.\n\n2. **Salud y Bienestar:** Las asociaciones con salud y bienestar reflejan la percepción de los consumidores de que estos productos son menos dañinos que los cigarrillos tradicionales. Esto es vital para el objetivo del subcapítulo, ya que resaltar los beneficios para la salud puede ser un punto de venta crucial. Los verbatims como _\"Salud, comodidad, alternativas, inocuidad, menor riesgo.\"_ indican que los consumidores perciben estos productos como opciones más seguras y saludables, lo cual puede influir significativamente en su decisión de compra. Esta percepción se debe a la comunicación efectiva de los beneficios para la salud que estos productos ofrecen, tales como la ausencia de alquitrán y la reducción de sustancias nocivas.\n\n3. **Innovación y Modernización:** La percepción de innovación y modernización es un aspecto importante que distingue a estos productos de los cigarrillos tradicionales. Los consumidores asocian términos como _\"novedoso\"_ y _\"modernización\"_ con estos productos, lo que sugiere que ven a IQOS y productos similares como avances tecnológicos en la industria del tabaco. La innovación puede ser un factor de atracción para consumidores jóvenes y tecnológicamente orientados, fortaleciendo la posición de la marca en segmentos específicos. Esta percepción se debe a las características innovadoras de los productos, como la tecnología de calentamiento sin combustión y la disponibilidad de sabores variados.\n\n4. **Medio Ambiente y Sostenibilidad:** Las menciones a la sostenibilidad y el impacto ambiental indican una creciente preocupación por estos temas entre los consumidores. Asociaciones como _\"Contaminación ambiental, impacto reducido, medio ambiente.\"_ sugieren que los consumidores valoran los productos que son percibidos como más sostenibles. Esto puede ser aprovechado en campañas de marketing que destaquen los beneficios ambientales de los productos IQOS, atrayendo a consumidores con una mayor conciencia ambiental. Las menciones a la reducción de la contaminación y el impacto ambiental se deben a la percepción de que estos productos generan menos residuos y contaminación en comparación con los cigarrillos tradicionales.\n\n5. **Comodidad y Practicidad:** La comodidad y practicidad son factores importantes que pueden influir en la adopción de estos productos. Los verbatims como _\"Comodidad, alternativas, practicidad.\"_ indican que los consumidores aprecian la facilidad de uso y la conveniencia que estos productos ofrecen, lo cual puede ser un diferenciador clave en el mercado. Estas características hacen que los productos sean más atractivos para personas con estilos de vida activos y ocupados, quienes buscan soluciones que se adapten a su ritmo de vida. Los consumidores valoran la facilidad de uso y la conveniencia, como la ausencia de cenizas y el menor olor.\n\n6. **Seguridad y Reducción de Riesgos:** La percepción de seguridad y reducción de riesgos es fundamental para convencer a los consumidores de cambiar a estos productos. Verbatims como _\"Seguridad, confiable, inocuidad, menor riesgo.\"_ refuerzan la idea de que estos productos son vistos como opciones más seguras, lo cual es un punto crucial para atraer a consumidores preocupados por los riesgos asociados al consumo de tabaco. Los consumidores, especialmente los mayores y los profesionales de la salud, priorizan productos que ofrecen un menor riesgo en comparación con los cigarrillos convencionales. Las características como la ausencia de fuego y la reducción de sustancias nocivas refuerzan esta percepción, haciendo que estos productos sean vistos como opciones más seguras.\n\n7. **Percepciones Negativas:** Aunque menos frecuentes, las percepciones negativas como _\"Peligro, precaución.\"_ indican que todavía existen barreras y preocupaciones que deben ser abordadas en la comunicación y educación sobre estos productos. Es importante que las campañas de marketing también se enfoquen en mitigar estas percepciones negativas para mejorar la aceptación general. Estas percepciones negativas pueden estar basadas en la falta de información o en experiencias previas con productos de tabaco. Es crucial que las campañas de marketing y educación se enfoquen en mitigar estas preocupaciones, proporcionando información clara y basada en evidencia sobre los beneficios y la seguridad de estos productos.\n\n#### Conclusión\n\nLas asociaciones hacia \"Productos de riesgo reducido\" y \"Tabaco sin combustión\" están fuertemente vinculadas a IQOS, salud, y la reducción de riesgos y daños. La percepción de innovación y modernización es notable, especialmente en el contexto de \"Tabaco sin combustión\". Las diferencias entre segmentos indican que las estrategias de marketing deben ser personalizadas según la edad, ocupación, y estilo de vida de los consumidores para maximizar su efectividad. IQOS ha logrado posicionarse efectivamente en la mente de los consumidores, asociándose con salud, innovación, y reducción de riesgos. Las diferencias entre segmentos indican que las estrategias de marketing deben ser personalizadas según la edad, ocupación, y estilo de vida de los consumidores para maximizar su efectividad."
                }
            ]
        }
    ]
}
```


**Estructura de lo que hay en la llave principal data**

 """
    Una lista de capítulos, cada uno con sus respectivos subcapítulos,
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
**Ejemplo de como construir el informe**
informe = ""

```python
for capitulo in respuesta['data']:
    print('Capitulo: ', capitulo['nombre_capitulo'], '\n\n')

    for subcapitulo in capitulo['sub_capitulos']:
        print('Subcapitulo:', subcapitulo['nombre_subcapitulo'], '\n\n')
        print(subcapitulo['informe'], '\n\n')
```

### Endpoint del Bot

**URL**: `/bot`

**Método**: `POST`

**Headers**:
- `Content-Type: application/json`
- `api_key_auth: <tu_api_key>`

**Body**:
```json
{
    "user_id": "usuario123",
    "mensaje": "Hola, ¿cómo estás?",
    "url_matriz": "http://example.com/matriz"
}
```

**Descripción**:
Este endpoint permite a los usuarios enviar un mensaje al bot, junto con un identificador de usuario y una URL de matriz. El bot procesará el mensaje y devolverá una respuesta generada.

**Comando CURL**:
```sh
curl -X POST http://127.0.0.1:8000/bot \
    -H "Content-Type: application/json" \
    -H "api_key_auth: <tu_api_key>" \
    -d '{
        "user_id": "usuario123",
        "mensaje": "Hola, ¿cómo estás?",
        "url_matriz": "http://example.com/matriz"
    }'
```

**Respuesta Exitosa**:
```json
{
    "ai_message": "¡Hola! Estoy aquí para ayudarte. ¿En qué puedo asistirte hoy?"
}
```

**Códigos de Estado**:
- `200 OK`: La solicitud fue exitosa y el bot respondió correctamente.
- `403 Forbidden`: La API key proporcionada no es válida.
- `422 Unprocessable Entity`: Hubo un error al procesar la solicitud.
- `500 Internal Server Error`: Ocurrió un error inesperado en el servidor.

**Notas**:
- Asegúrate de reemplazar `<tu_api_key>` con una API key válida.
- El `user_id` es utilizado para identificar al usuario que envía el mensaje.
- La `url_matriz` es un recurso adicional que el bot puede utilizar para generar su respuesta.