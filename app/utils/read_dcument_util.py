import requests
import fitz  # PyMuPDF
import io
import pandas as pd


def pdf_to_text(pdf_url:str) -> list:
    # Descargar el PDF desde la URL
    response = requests.get(pdf_url)

    if response.status_code == 200:
        pdf_stream = io.BytesIO(response.content)

        texto = ""
        doc = fitz.open(stream=pdf_stream, filetype="pdf")
        for page in doc:
            texto += page.get_text()
        return texto
    else:
        return None
    

def get_data_excel(url_excel:str) -> list[list]:
    
    df_excel = pd.read_excel(url_excel)

    df_excel.iloc[:,0].fillna(method='ffill', inplace=True)

    index_pos = df_excel.index[df_excel.iloc[:, 1].notna()].tolist()
    index_pos.append(df_excel.index[-1])
    m_col = df_excel.shape[1]

    list_cap = []

    for ind in range(len(index_pos) - 1):
        ini_cap = index_pos[ind]
        fin_cap = index_pos[ind + 1]

        nombre_capitulo = df_excel.iloc[ini_cap, 1].replace('\n', ' ').replace('nan', '').rstrip()

        df_cap = df_excel.iloc[ini_cap:fin_cap]

        index_pos_sub = df_cap[df_cap.iloc[:, 2].notna()].index.tolist()
        index_pos_sub.append(df_cap.index[-1] + 1)

        lis_sub_cap = []

        for ind2 in range(len(index_pos_sub) - 1):
            ini_sub_cap = index_pos_sub[ind2]
            fin_sub_cap = index_pos_sub[ind2 + 1]

            df_sub_cap = df_cap.loc[ini_sub_cap:fin_sub_cap - 1].replace('\n', ' ', regex=True).fillna('')

            objetivo = df_sub_cap.iloc[0, 0]
            nombre_sub_capitulo = df_sub_cap.iloc[0, 2]

            textos_sub = []

            for i in range(df_sub_cap.shape[0]):
                pregunta = df_sub_cap.iloc[i, 3]
                textos_sub.append(f"\n**Pregunta:** {pregunta}\n")
                for j in range(4, df_sub_cap.shape[1]):
                    respuesta = df_sub_cap.iloc[i, j]
                    textos_sub.append(f"- {respuesta}\n")

            texto_sub = ''.join(textos_sub)
            lis_sub_cap.append((objetivo, nombre_sub_capitulo, texto_sub))

        list_cap.append((nombre_capitulo, lis_sub_cap))

    return list_cap