app.py
import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from io import BytesIO
from openai import OpenAI
import time

# ---------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------

st.set_page_config(
    page_title="Resumen Ejecutivo IA",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------------------
# ESTILOS PERSONALIZADOS
# ---------------------------------------------------

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: bold;
    color: #1565C0;
}

.subtitle {
    font-size: 18px;
    color: gray;
}

.summary-box {
    background-color: #F5F7FA;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #DDE3EA;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TÍTULO
# ---------------------------------------------------

st.markdown(
    '<p class="main-title">📄 Generador de Resúmenes Ejecutivos con IA</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Carga uno o varios archivos PDF y genera automáticamente un resumen ejecutivo.</p>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# API KEY
# ---------------------------------------------------

api_key = st.sidebar.text_input(
    "🔑 OpenAI API Key",
    type="password"
)

# ---------------------------------------------------
# CARGA DE ARCHIVOS
# ---------------------------------------------------

uploaded_files = st.file_uploader(
    "📂 Selecciona uno o varios archivos PDF",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------------------------------------------
# FUNCIÓN EXTRAER TEXTO PDF
# ---------------------------------------------------

def extraer_texto_pdf(pdf_file):

    texto = ""

    lector = PdfReader(pdf_file)

    for pagina in lector.pages:

        contenido = pagina.extract_text()

        if contenido:
            texto += contenido + "\n"

    return texto

# ---------------------------------------------------
# FUNCIÓN GENERAR RESUMEN IA
# ---------------------------------------------------

def generar_resumen(texto, api_key):

    client = OpenAI(api_key=api_key)

    prompt = f"""
    Analiza el siguiente documento y genera un resumen ejecutivo profesional.

    Incluye obligatoriamente:

    1. Objetivo del documento
    2. Puntos principales
    3. Conclusiones
    4. Recomendaciones

    Documento:
    {texto[:12000]}
    """

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Eres un especialista en elaboración de resúmenes ejecutivos."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return respuesta.choices[0].message.content

# ---------------------------------------------------
# FUNCIÓN EXPORTAR WORD
# ---------------------------------------------------

def generar_word(resumen):

    documento = Document()

    documento.add_heading("Resumen Ejecutivo", level=1)

    documento.add_paragraph(resumen)

    buffer = BytesIO()

    documento.save(buffer)

    buffer.seek(0)

    return buffer

# ---------------------------------------------------
# BOTÓN GENERAR RESUMEN
# ---------------------------------------------------

if st.button("🚀 Generar Resumen Ejecutivo"):

    if not api_key:
        st.error("⚠️ Debe ingresar su OpenAI API Key.")
        st.stop()

    if not uploaded_files:
        st.error("⚠️ Debe cargar al menos un archivo PDF.")
        st.stop()

    progreso = st.progress(0)

    texto_total = ""

    total_archivos = len(uploaded_files)

    for indice, archivo in enumerate(uploaded_files):

        st.info(f"Procesando archivo: {archivo.name}")

        texto_total += extraer_texto_pdf(archivo)

        porcentaje = int((indice + 1) / total_archivos * 100)

        progreso.progress(porcentaje)

        time.sleep(0.3)

    with st.spinner("🤖 Generando resumen ejecutivo con IA..."):

        resumen = generar_resumen(texto_total, api_key)

    st.success("✅ Resumen generado correctamente")

    # Mostrar resumen
    st.markdown(
        f'<div class="summary-box">{resumen}</div>',
        unsafe_allow_html=True
    )

    # Descargar Word
    archivo_word = generar_word(resumen)

    st.download_button(
        label="📥 Descargar Resumen en Word",
        data=archivo_word,
        file_name="resumen_ejecutivo.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    # Animación
    st.balloons()
