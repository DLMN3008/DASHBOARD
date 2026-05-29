# app.py
import streamlit as st
import random
import time

st.set_page_config(
    page_title="Ecuaciones de Primer Grado",
    page_icon="📘",
    layout="centered"
)

st.title("📘 Práctica de Ecuaciones de Primer Grado")
st.write("Resuelve la ecuación y encuentra el valor de x.")

# Inicializar estado
if "pregunta" not in st.session_state:
    st.session_state.pregunta = None

if "respuesta" not in st.session_state:
    st.session_state.respuesta = None


# Función para generar ecuaciones
def generar_ecuacion():
    x = random.randint(1, 10)

    a = random.randint(1, 10)
    b = random.randint(1, 20)

    # ax + b = c
    c = a * x + b

    ecuacion = f"{a}x + {b} = {c}"

    return ecuacion, x


# Generar primera pregunta
if st.session_state.pregunta is None:
    ecuacion, solucion = generar_ecuacion()
    st.session_state.pregunta = ecuacion
    st.session_state.respuesta = solucion


# Mostrar ecuación
st.subheader(f"✏️ {st.session_state.pregunta}")

# Entrada del usuario
respuesta_usuario = st.number_input(
    "Ingresa el valor de x:",
    step=1,
    format="%d"
)

# Botón verificar
if st.button("✅ Verificar respuesta"):

    if respuesta_usuario == st.session_state.respuesta:

        st.success("🎉 ¡Correcto! Excelente trabajo.")

        # Animación
        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        st.balloons()

    else:
        st.error("❌ Respuesta incorrecta. Intenta nuevamente.")


# Botón nueva pregunta
if st.button("🔄 Nueva pregunta"):
    ecuacion, solucion = generar_ecuacion()

    st.session_state.pregunta = ecuacion
    st.session_state.respuesta = solucion

    st.rerun()
