import streamlit as st
import plotly.express as px

st.title("Ejemplo")

df = px.data.tips()

st.dataframe(df)

mascara = df['total_bill'] > 10

st.write(mascara)