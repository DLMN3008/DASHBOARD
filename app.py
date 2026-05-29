import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from io import BytesIO
from openai import OpenAI
import time

st.set_page_config(
    page_title="Resumen Ejecutivo IA",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Generador de Resúmenes Ejecutivos con IA")

api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type="password"
)

uploaded_files = st.file_uploader(
    "Cargar PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

def extraer_texto_pdf(pdf_file):

    texto = ""

    lector = PdfReader(pdf_file)

    for pagina in lector.pages:

        contenido = pagina.extract_text()

        if contenido:
            texto += contenido + "\n"

    return texto

def generar_resumen(texto, api_key):

    client = OpenAI(api_key=api_key)

    prompt = f"""
    Genera un resumen ejecutivo profesional del siguiente documento.

    Incluye:
    - Objetivo
    - Puntos principales
    - Conclusiones
    - Recomendaciones

    Documento:
    {texto[:12000]}
    """

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Eres un analista ejecutivo."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return respuesta.choices[0].message.content

def generar_word(resumen):

    documento = Document()

    documento.add_heading("Resumen Ejecutivo", level=1)

    documento.add_paragraph(resumen)

    buffer = BytesIO()

    documento.save(buffer)

    buffer.seek(0)

    return buffer

if st.button("Generar Resumen"):

    if not api_key:
        st.error("Ingrese API Key")
        st.stop()

    if not uploaded_files:
        st.error("Suba un PDF")
        st.stop()

    progreso = st.progress(0)

    texto_total = ""

    for i, archivo in enumerate(uploaded_files):

        texto_total += extraer_texto_pdf(archivo)

        progreso.progress((i + 1) / len(uploaded_files))

        time.sleep(0.2)

    resumen = generar_resumen(texto_total, api_key)

    st.success("Resumen generado")

    st.write(resumen)

    archivo_word = generar_word(resumen)

    st.download_button(
        "Descargar Word",
        data=archivo_word,
        file_name="resumen.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    st.balloons()
