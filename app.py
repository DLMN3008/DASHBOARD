# app.py

```python
import streamlit as st
import random
import time

# -----------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------------

st.set_page_config(
    page_title="Ecuaciones de Primer Grado",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------------
# ESTILOS PERSONALIZADOS
# -----------------------------------

st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:bold;
    color:#4CAF50;
    text-align:center;
}

.question-box {
    padding:20px;
    border-radius:15px;
    background-color:#f3f7ff;
    text-align:center;
    font-size:35px;
    font-weight:bold;
    color:#1f3b73;
    margin-top:20px;
    margin-bottom:20px;
}

.success-animation {
    text-align:center;
    font-size:40px;
    color:#ff9800;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# TÍTULO
# -----------------------------------

st.markdown(
    '<p class="big-title">🧠 Practica Ecuaciones de Primer Grado</p>',
    unsafe_allow_html=True
)

st.write("Resuelve correctamente el valor de x.")

# -----------------------------------
# FUNCIÓN PARA GENERAR ECUACIONES
# -----------------------------------

def generar_pregunta():

    # Respuesta siempre entre 1 y 10
    x = random.randint(1, 10)

    # Coeficientes aleatorios
    a = random.randint(1, 10)
    b = random.randint(1, 20)

    # ax + b = c
    c = a * x + b

    ecuacion = f"{a}x + {b} = {c}"

    return ecuacion, x

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "ecuacion" not in st.session_state:
    ecuacion, respuesta = generar_pregunta()
    st.session_state.ecuacion = ecuacion
    st.session_state.respuesta = respuesta

# -----------------------------------
# MOSTRAR PREGUNTA
# -----------------------------------

st.markdown(
    f'<div class="question-box">{st.session_state.ecuacion}</div>',
    unsafe_allow_html=True
)

# -----------------------------------
# INPUT DEL USUARIO
# -----------------------------------

respuesta_usuario = st.number_input(
    "Ingresa el valor de x:",
    min_value=0,
    max_value=100,
    step=1
)

# -----------------------------------
# BOTÓN VERIFICAR
# -----------------------------------

if st.button("✅ Verificar Respuesta"):

    if respuesta_usuario == st.session_state.respuesta:

        st.success("🎉 ¡CORRECTO!")

        # Barra de carga animada
        barra = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            barra.progress(i + 1)

        # Animaciones WOW
        st.balloons()
        st.snow()

        st.markdown("""
        <div class="success-animation">
            ⭐ ¡Excelente Trabajo! ⭐
        </div>
        """, unsafe_allow_html=True)

    else:
        st.error("❌ Respuesta incorrecta. Sigue intentando.")

# -----------------------------------
# BOTÓN NUEVA PREGUNTA
# -----------------------------------

if st.button("🔄 Nueva Pregunta"):

    ecuacion, respuesta = generar_pregunta()

    st.session_state.ecuacion = ecuacion
    st.session_state.respuesta = respuesta

    st.rerun()
```

# requirements.txt

```txt
streamlit
```

# README.md

````md
# Aplicativo de Ecuaciones de Primer Grado

Aplicación desarrollada con Streamlit para practicar ecuaciones de primer grado.

## Características

- Preguntas aleatorias
- Respuestas enteras del 1 al 10
- Validación automática
- Animaciones cuando el usuario acierta

## Ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
````

````

# COMANDOS GITHUB

```bash
git init
git add .
git commit -m "Primer commit"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git push -u origin main
````

# DESPLIEGUE EN STREAMLIT CLOUD

1. Subir el proyecto a GitHub
2. Entrar a https://share.streamlit.io
3. Conectar GitHub
4. Seleccionar el repositorio
5. Elegir:

   * Branch: main
   * File: app.py
6. Deploy 🚀
