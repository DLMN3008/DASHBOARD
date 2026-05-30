import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------
st.set_page_config(
    page_title="Dashboard Iris",
    page_icon="🌸",
    layout="wide"
)

# --------------------------------------------------
# CARGA DE DATOS
# --------------------------------------------------
@st.cache_data
def cargar_datos():
    iris = load_iris()

    df = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )

    df["species"] = [
        iris.target_names[i]
        for i in iris.target
    ]

    return df

df = cargar_datos()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("Filtros")

especies = st.sidebar.multiselect(
    "Seleccionar especie",
    options=df["species"].unique(),
    default=df["species"].unique()
)

df_filtrado = df[
    df["species"].isin(especies)
]

# --------------------------------------------------
# TÍTULO
# --------------------------------------------------
st.title("🌸 Dashboard del Dataset Iris")

st.markdown(
    """
    Exploración interactiva del conjunto de datos Iris utilizando
    visualizaciones profesionales con la paleta Viridis.
    """
)

# --------------------------------------------------
# KPIs
# --------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Observaciones",
        len(df_filtrado)
    )

with c2:
    st.metric(
        "Especies",
        df_filtrado["species"].nunique()
    )

with c3:
    st.metric(
        "Prom. Largo Sépalo",
        round(
            df_filtrado["sepal length (cm)"].mean(),
            2
        )
    )

with c4:
    st.metric(
        "Prom. Largo Pétalo",
        round(
            df_filtrado["petal length (cm)"].mean(),
            2
        )
    )

st.divider()

# --------------------------------------------------
# GRÁFICOS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    fig_scatter = px.scatter(
        df_filtrado,
        x="sepal length (cm)",
        y="petal length (cm)",
        color="species",
        color_discrete_sequence=px.colors.sequential.Viridis,
        size="petal width (cm)",
        title="Relación entre Sépalo y Pétalo"
    )

    fig_scatter.update_layout(
        height=500
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

with col2:

    fig_box = px.box(
        df_filtrado,
        x="species",
        y="sepal width (cm)",
        color="species",
        color_discrete_sequence=px.colors.sequential.Viridis,
        title="Distribución del Ancho del Sépalo"
    )

    fig_box.update_layout(
        height=500,
        showlegend=False
    )

    st.plotly_chart(
        fig_box,
        use_container_width=True
    )

# --------------------------------------------------
# HISTOGRAMA
# --------------------------------------------------
fig_hist = px.histogram(
    df_filtrado,
    x="petal length (cm)",
    color="species",
    barmode="overlay",
    color_discrete_sequence=px.colors.sequential.Viridis,
    title="Distribución del Largo del Pétalo"
)

fig_hist.update_layout(
    height=500
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

# --------------------------------------------------
# MATRIZ DE DISPERSIÓN
# --------------------------------------------------
fig_matrix = px.scatter_matrix(
    df_filtrado,
    dimensions=[
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"
    ],
    color="species",
    color_discrete_sequence=px.colors.sequential.Viridis,
    title="Matriz de Dispersión"
)

fig_matrix.update_layout(
    height=800
)

st.plotly_chart(
    fig_matrix,
    use_container_width=True
)

# --------------------------------------------------
# TABLA
# --------------------------------------------------
st.subheader("Datos")

st.dataframe(
    df_filtrado,
    use_container_width=True
)

# --------------------------------------------------
# DESCARGA
# --------------------------------------------------
csv = df_filtrado.to_csv(index=False)

st.download_button(
    label="📥 Descargar CSV",
    data=csv,
    file_name="iris_filtrado.csv",
    mime="text/csv"
)
