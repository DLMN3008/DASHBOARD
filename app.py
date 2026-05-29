import streamlit as st
import random

st.set_page_config(
    page_title="Práctica de Ecuaciones de Primer Grado",
    page_icon="🧮",
    layout="centered"
)


def generar_ecuacion():
    """
    Genera ecuaciones del tipo:
    ax + b = c
    donde x siempre es un entero entre 1 y 10
    """

    x = random.randint(1, 10)

    a = random.randint(2, 10)
    b = random.randint(-20, 20)

    c = a * x + b

    ecuacion = f"{a}x + ({b}) = {c}"

    return ecuacion, x


# Inicialización de variables de sesión
if "ecuacion" not in st.session_state:
    ecuacion, solucion = generar_ecuacion()
    st.session_state.ecuacion = ecuacion
    st.session_state.solucion = solucion

if "aciertos" not in st.session_state:
    st.session_state.aciertos = 0


st.title("🧮 Práctica de Ecuaciones de Primer Grado")

st.markdown(
    """
    Resuelve la ecuación y encuentra el valor de **x**.
    """
)

st.subheader(st.session_state.ecuacion)

respuesta = st.number_input(
    "Ingresa el valor de x:",
    step=1,
    format="%d"
)

col1, col2 = st.columns(2)

with col1:
    verificar = st.button("✅ Verificar")

with col2:
    nueva = st.button("🔄 Nueva pregunta")

if verificar:

    if int(respuesta) == st.session_state.solucion:

        st.success(
            f"¡Correcto! La respuesta es x = {st.session_state.solucion}"
        )

        st.session_state.aciertos += 1

        # Animación
        st.balloons()

        st.markdown(
            """
            ## 🎉 ¡Excelente trabajo!
            Sigue practicando para mejorar tus habilidades.
            """
        )

    else:
        st.error(
            f"Incorrecto. Inténtalo nuevamente."
        )

if nueva:

    ecuacion, solucion = generar_ecuacion()

    st.session_state.ecuacion = ecuacion
    st.session_state.solucion = solucion

    st.rerun()

st.divider()

st.metric(
    label="🏆 Aciertos",
    value=st.session_state.aciertos
)

with st.expander("Ver instrucciones"):
    st.write(
        """
        1. Resuelve la ecuación.
        2. Ingresa el valor de x.
        3. Presiona 'Verificar'.
        4. Genera una nueva pregunta cuando desees.
        """
    )
