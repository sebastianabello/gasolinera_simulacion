import random
import simpy
from gasolinera.recursos import VELOCIDAD_TANQUEO
from gasolinera.eventos import registrar_cliente

# Tiempo entre llegadas, valor por defecto
TIEMPO_ENTRE_LLEGADAS = 60
CANTIDAD_MIN_LITROS = 10
CANTIDAD_MAX_LITROS = 50


def set_tiempo_llegada(tiempo):
    global TIEMPO_ENTRE_LLEGADAS
    TIEMPO_ENTRE_LLEGADAS = tiempo


def cliente(env, nombre, recursos):
    surtidores = recursos['surtidores']
    tanque = recursos['tanque']

    with surtidores.request() as request:
        yield request

        litros_deseados = random.randint(CANTIDAD_MIN_LITROS, CANTIDAD_MAX_LITROS)

        if tanque.level >= litros_deseados:
            yield tanque.get(litros_deseados)
            tiempo_tanqueo = litros_deseados / VELOCIDAD_TANQUEO
            yield env.timeout(tiempo_tanqueo)
            registrar_cliente(atendido=True)
        else:
            registrar_cliente(atendido=False)


def generar_clientes(env, recursos):
    contador = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / TIEMPO_ENTRE_LLEGADAS))
        contador += 1
        env.process(cliente(env, f"C{contador}", recursos))
