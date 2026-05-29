# app.py

```python
import streamlit as st
import random
import time

# ---------------------------------------
# CONFIGURACIÓN
# ---------------------------------------

st.set_page_config(
    page_title="Ecuaciones de Primer Grado",
    page_icon="📘",
    layout="centered"
)

# ---------------------------------------
# ESTILOS CSS
# ---------------------------------------

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#4CAF50;
}

.question-box{
    background:#f0f4ff;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:36px;
    font-weight:bold;
    color:#1d3557;
    margin-top:20px;
    margin-bottom:20px;
    border:2px solid #90caf9;
}

.correct{
    text-align:center;
    font-size:40px;
    color:gold;
    font-weight:bold;
}

.wrong{
    text-align:center;
    font-size:38px;
    color:#ff4d4d;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# TÍTULO
# ---------------------------------------

st.markdown(
    '<div class="main-title">🧠 Practica Ecuaciones de Primer Grado</div>',
    unsafe_allow_html=True
)

st.write("Resuelve correctamente el valor de x.")

# ---------------------------------------
# FUNCIÓN GENERAR PREGUNTA
# ---------------------------------------

def generar_pregunta():

    # Respuesta entre 1 y 10
    x = random.randint(1, 10)

    # Coeficientes aleatorios
    a = random.randint(1, 10)
    b = random.randint(1, 20)

    # ax + b = c
    c = a * x + b

    ecuacion = f"{a}x + {b} = {c}"

    return ecuacion, x

# ---------------------------------------
# SESSION STATE
# ---------------------------------------

if "ecuacion" not in st.session_state:

    ecuacion, respuesta = generar_pregunta()

    st.session_state.ecuacion = ecuacion
    st.session_state.respuesta = respuesta

# ---------------------------------------
# MOSTRAR ECUACIÓN
# ---------------------------------------

st.markdown(
    f'<div class="question-box">{st.session_state.ecuacion}</div>',
    unsafe_allow_html=True
)

# ---------------------------------------
# INPUT
# ---------------------------------------

respuesta_usuario = st.number_input(
    "Ingresa el valor de x:",
    min_value=0,
    max_value=100,
    step=1
)

# ---------------------------------------
# BOTÓN VERIFICAR
# ---------------------------------------

if st.button("✅ Verificar Respuesta"):

    if respuesta_usuario == st.session_state.respuesta:

        st.success("🎉 ¡Respuesta Correcta!")

        # Animación de progreso
        barra = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            barra.progress(i + 1)

        # Estrellas y celebración
        st.balloons()

        st.markdown("""
        <div class="correct">
            ⭐ ⭐ ⭐ EXCELENTE ⭐ ⭐ ⭐
        </div>
        """, unsafe_allow_html=True)

        st.snow()

    else:

        st.error("❌ Respuesta Incorrecta")

        # Animación triste
        st.markdown("""
        <div class="wrong">
            😢 😢 😢 <br>
            Sigue intentando
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------
# BOTÓN NUEVA PREGUNTA
# ---------------------------------------

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

Aplicación educativa desarrollada con Streamlit para practicar ecuaciones de primer grado.

## Funcionalidades

- Preguntas aleatorias
- Respuestas enteras entre 1 y 10
- Validación automática
- Animaciones interactivas
- Diseño moderno

## Ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
````

## Despliegue

Sube el proyecto a GitHub y despliega gratis en Streamlit Cloud.

````

# COMANDOS GITHUB

```bash
git init
git add .
git commit -m "Aplicativo ecuaciones"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git push -u origin main
````

# DESPLEGAR EN STREAMLIT CLOUD

1. Entrar a:
   https://share.streamlit.io

2. Conectar GitHub

3. Seleccionar el repositorio

4. Elegir:

* Branch: main
* File: app.py

5. Presionar Deploy 🚀
