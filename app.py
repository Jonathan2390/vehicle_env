import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Análisis de información de vehículos')

st.header('Representación de datos a través de un histograma')
print()
st.write('En este apartado elaboramos un histograma interactivo, mediante la selección de un checkbox')
car_data = pd.read_csv(
    'https://raw.githubusercontent.com/Jonathan2390/vehicle_env/refs/heads/main/vehicles_us.csv')

build_histogram = st.checkbox('Construir histograma')  # crear un botón

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # crear un histograma con in checkbox
    fig_a= px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_a, use_container_width=True)
    print()
    print()

st.header('Representación a través de un gráfico de dispersión')
print()
build_scatter = st.checkbox(
    'Construir gráfica de dispersión')  # crear un botón

if build_scatter:  # si la casilla de verificación está seleccionada
    st.write('Construir una gráfica de dispersión para las columna odómetro y precio')

    # crear un gráfico de dispersión
    fig_b = px.scatter(car_data, x="odometer", y="price")
    fig_b.show()  # crear gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_b, use_container_width=True)

