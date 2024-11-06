import streamlit as st
import plotly.express as px

st.title("Mi primera App")

st.header("Titulo 2")

st.markdown('''
# Ejemplo Markdown
# Es un ejemplo 
:rocket:           
''')

df = px.data.tips()

#st.dataframe(df)

#st.table(df)

datos =  df.rename(columns={
    'total_bill':'cuenta_total',
    'tip':'propina',
    'sex':'genero',
    'smoker':'fumador',
    'day':' dia',
    'time':'hora',
    'size':'tamano_mesa'
})

st.table(datos.head(10))

st.sidebar.header('Sidebar')

rango_cuenta = st.sidebar.slider(
    'Rango de Cuenta',
    min_value = float(datos['cuenta_total'].min()),
    max_value = float(datos['cuenta_total'].max()),
    value= (float(datos['cuenta_total'].min()),float(datos['cuenta_total'].max()))
)

personas = st.sidebar.slider(
    'Personas en la mesa',
    min_value = int(datos['tamano_mesa'].min()),
    max_value = int(datos['tamano_mesa'].max()),
    value= (int(datos['tamano_mesa'].min()),int(datos['tamano_mesa'].max()))
)
hora_seleccionada = st.sidebar.radio(
    'Hora del Dia',
    options=['Todos','Lunch','Dinner']
)


mask = (
    (datos['cuenta_total']>=rango_cuenta[0]) &
    (datos['cuenta_total']<=rango_cuenta[1]) &
    (datos['tamano_mesa'] >=personas[0]) &
    (datos['tamano_mesa']<=personas[1])
)

if hora_seleccionada != 'Todos':
    mask = mask & (datos['hora']== hora_seleccionada)

datos_filtrados = datos[mask]



col1,col2 = st.columns(2)

with col1:
    st.metric(
        label = 'Total de registros',
        value=len(datos_filtrados),
        delta= f"${len(datos_filtrados) - len(datos)} vs total"
    )

with col2:
    st.metric(
        label='Promedio de propinas',
        value=f"${datos_filtrados['propina'].mean():.2f}"
    )


st.subheader('Relacion Cuenta/Propina')

fig = px.scatter(
    datos,
    x='cuenta_total',
    y='propina',
    color='hora',
    size='tamano_mesa',
    
)

st.plotly_chart(fig)
