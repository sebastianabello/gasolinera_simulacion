# 🛢️🚗 Simulación de Gasolinera — Eventos Discretos con Streamlit y SimPy

Este proyecto simula el funcionamiento de una **gasolinera** utilizando:
- **SimPy** para la **simulación de eventos discretos**.
- **Streamlit** para crear un **dashboard interactivo** donde puedes ver los resultados y controlar los parámetros de simulación.

---

## 📚 Descripción del Proyecto

Se modelan los siguientes elementos:
- **Clientes** que llegan a cargar combustible de forma aleatoria.
- **Surtidores** limitados en número que atienden a los clientes.
- **Camión de suministro** que recarga el tanque de gasolina cada cierto intervalo.
- **Tanque de almacenamiento** que tiene capacidad limitada y puede agotarse.

El objetivo de la simulación es observar:
- El nivel de gasolina a lo largo del tiempo.
- El número de clientes atendidos vs rechazados.

¡Todo configurado fácilmente a través de sliders en la interfaz web! 🎛

---

## 🛠️ Instalación

### 1. Clona el repositorio
```bash

git clone https://github.com/sebastianabello/gasolinera_simulacion.git
cd gasolinera_simulacion
```
### 2. Recomiendo crear un entorno virtual 
```bash

python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate.bat   # Windows
```
### 3. Instalar las dependencias
```bash

pip install -r requirements.txt
```
---
## 🚀 Cómo iniciar la simulación
Ejecuta el siguiente comando para lanzar el dashboard:
```bash

streamlit run app.py
```
---

## ⚙️ Opciones de Configuración en el Dashboard
Desde el panel lateral puedes configurar:

- Duración de la simulación (días)
- Número de surtidores
- Capacidad del tanque de gasolina
- Tiempo promedio entre llegadas de clientes (en segundos)
- Tiempo entre recargas del camión de suministro (en horas)

¡Después solo presiona "Correr Simulación" y observa los resultados!

⚠️ Posiblemente al presionar "Correr Simulación" la primera vez no se vean los resultados, vuelvalo a oprimir y ya deberia funcionar.⚠️

