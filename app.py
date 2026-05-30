import streamlit as st
from pypdf import PdfReader
from openai import OpenAI

# Configuración OpenAI
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

st.set_page_config(
    page_title="Resumen Inteligente de PDF",
    page_icon="📄"
)

st.title("📄 Resumen Inteligente de PDF")

archivo = st.file_uploader(
    "Seleccione un PDF",
    type=["pdf"]
)

tipo_resumen = st.selectbox(
    "Tipo de resumen",
    [
        "Ejecutivo",
        "Financiero",
        "Contable",
        "Gerencial",
        "Personalizado"
    ]
)

instruccion = ""

if tipo_resumen == "Personalizado":
    instruccion = st.text_area(
        "Indique cómo desea el resumen"
    )

if archivo:

    texto = ""

    try:
        lector = PdfReader(archivo)

        for pagina in lector.pages:
            texto += pagina.extract_text() + "\n"

        st.success(
            f"PDF cargado correctamente. "
            f"Se detectaron {len(lector.pages)} páginas."
        )

        if st.button("Generar Resumen"):

            with st.spinner("Analizando documento..."):

                if tipo_resumen != "Personalizado":

                    prompts = {
                        "Ejecutivo":
                        """
                        Genera un resumen ejecutivo
                        resaltando:
                        - Objetivo
                        - Hallazgos principales
                        - Conclusiones
                        """,

                        "Financiero":
                        """
                        Resume el documento desde un
                        enfoque financiero.
                        Destaca:
                        - Ingresos
                        - Gastos
                        - Rentabilidad
                        - Riesgos
                        """,

                        "Contable":
                        """
                        Resume el documento desde una
                        perspectiva contable.
                        """,

                        "Gerencial":
                        """
                        Resume el documento para un
                        gerente general.
                        """
                    }

                    instruccion = prompts[tipo_resumen]

                respuesta = client.chat.completions.create(
                    model="gpt-5",
                    messages=[
                        {
                            "role": "system",
                            "content": instruccion
                        },
                        {
                            "role": "user",
                            "content": texto[:120000]
                        }
                    ]
                )

                resumen = respuesta.choices[0].message.content

                st.subheader("Resumen generado")

                st.write(resumen)

                st.download_button(
                    "Descargar Resumen",
                    resumen,
                    file_name="resumen.txt"
                )

    except Exception as e:
        st.error(f"Error: {e}")
