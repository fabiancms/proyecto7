import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("Tablero interactivo - Vehiculos - Mi primer tablero")


hist_button = st.button('Construir mi primer histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


button_2 = st.checkbox('Construir un scatterplot')

if button_2: # si la casilla de verificación está seleccionada
    st.write('Construir un grafico de dispercion')
    
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    
    st.plotly_chart(fig, use_container_width=True)
    
    
button_3 = st.checkbox('Construir un diagrama de Gantt')

if button_3: # si la casilla de verificación está seleccionada
    st.write('Construir un grafico de diagrama de Gantt')
    
    # Asegurar que la fecha esté en formato datetime
    car_data["date_posted"] = pd.to_datetime(car_data["date_posted"], errors="coerce")

    # Crear columna con fecha final (inicio + días publicados)
    car_data["end_date"] = car_data["date_posted"] + pd.to_timedelta(car_data["days_listed"], unit="D")

    # Seleccionamos unas filas para que el gráfico no quede muy cargado
    subset = car_data.head(15)

    # Crear gráfico de Gantt (timeline)
    fig = px.timeline(
    subset,
    x_start="date_posted",
    x_end="end_date",
    y="model",
    color="condition",  # Colorear según condición del auto
    title="Gantt Chart - Tiempo de publicación de vehículos"
    )

    # Ordenar de arriba hacia abajo
    fig.update_yaxes(autorange="reversed")


    st.plotly_chart(fig, use_container_width=True)