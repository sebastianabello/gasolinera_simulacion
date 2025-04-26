import simpy
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from gasolinera import recursos
from gasolinera.cliente import generar_clientes, set_tiempo_llegada
from gasolinera.camion import camion_suministro, set_tiempo_camion
from gasolinera.eventos import nivel_tanque_log, clientes_atendidos, clientes_rechazados, reset_eventos

def correr_simulacion(tiempo_simulacion, surtidores, capacidad_tanque):
    reset_eventos()

    env = simpy.Environment()
    recursos_dict = recursos.crear_recursos(env, surtidores, capacidad_tanque)

    env.process(generar_clientes(env, recursos_dict))
    env.process(camion_suministro(env, recursos_dict))

    env.run(until=tiempo_simulacion)

def mostrar_dashboard():
    st.title("🚗⛽ Resultados de la Simulación de Gasolinera")

    if nivel_tanque_log:
        df_nivel = pd.DataFrame(nivel_tanque_log, columns=['Tiempo', 'Nivel'])
        st.subheader("Nivel del tanque a lo largo del tiempo")
        st.line_chart(df_nivel.set_index('Tiempo'))

    st.subheader("Clientes atendidos vs rechazados")
    st.bar_chart({'Clientes': [clientes_atendidos, clientes_rechazados]})

    st.metric(label="Clientes Atendidos", value=clientes_atendidos)
    st.metric(label="Clientes Rechazados", value=clientes_rechazados)

def main():
    st.sidebar.title("⚙️ Configuración de Simulación")

    # Configuraciones que el usuario puede cambiar
    dias_simulacion = st.sidebar.slider("Duración de simulación (días)", 1, 7, 2)
    tiempo_simulacion = dias_simulacion * 24 * 60 * 60

    surtidores = st.sidebar.slider("Número de surtidores", 1, 10, 2)
    capacidad_tanque = st.sidebar.slider("Capacidad del tanque (litros)", 5000, 50000, 20000)

    tiempo_llegada_cliente = st.sidebar.slider("Tiempo promedio entre clientes (segundos)", 10, 300, 60)
    set_tiempo_llegada(tiempo_llegada_cliente)

    tiempo_entre_camiones = st.sidebar.slider("Tiempo entre camiones (horas)", 1, 24, 4)
    set_tiempo_camion(tiempo_entre_camiones * 60 * 60)

    if st.sidebar.button("Correr Simulación"):
        correr_simulacion(tiempo_simulacion, surtidores, capacidad_tanque)
        mostrar_dashboard()

if __name__ == "__main__":
    main()
