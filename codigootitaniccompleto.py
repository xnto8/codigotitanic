import streamlit as st
import pandas as pd

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("estructura del DataFrame:")
    st.write(dfdescribe())
    col = st.selectbox("seleccionar una columna para filtrar", df.columns)
    valor_min = st.slider("seleccionar un valor minimo", float(df[col].min()), float(df[col].max()))
    df_filtrado = df[df[col] >= valor_min]
    st.write(f" Datos filtrados donde {col} >= {valor_min}:")
    st.write(df_filtrado)

fig, ax = plt.subplots()
ax.hist(df[col], bins=20)
ax.set_title(f"Histograma de {col}")
ax.set_xlabel(col)
ax.set_ylabel("Frecuencia")
st.pyplot(fig)
import altair as alt
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    x_axis=st.selectbox("selecciona el eje x", df.select_dtypes(include= "number").columns)
    y_axis=st.selectbox("selecciona el eje y", df.select_dtypes(include= "number").columns)
    chart = alt.Chart(df).mark_cicle(size=60).encode(
        x=x_axis,
        y=y_axis,
        tooltip=[x_axis, y_axis].interactive()
    st.altair_chart(chart, use_container_width=True)

