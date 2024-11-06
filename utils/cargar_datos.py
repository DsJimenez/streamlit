import streamlit as st
import plotly.express as px

def cargar_datos():
    df = px.data.tips()
    st.markdown('''
    # Se cargaron los datos con exito. :rocket:
    ''')