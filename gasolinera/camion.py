import simpy
from gasolinera.eventos import registrar_nivel_tanque

TIEMPO_ENTRE_CAMIONES = 4 * 60 * 60  # 4 horas por defecto


def set_tiempo_camion(tiempo_segundos):
    global TIEMPO_ENTRE_CAMIONES
    TIEMPO_ENTRE_CAMIONES = tiempo_segundos


def camion_suministro(env, recursos):
    tanque = recursos['tanque']

    while True:
        yield env.timeout(TIEMPO_ENTRE_CAMIONES)

        cantidad_a_cargar = tanque.capacity - tanque.level
        if cantidad_a_cargar > 0:
            yield tanque.put(cantidad_a_cargar)
        registrar_nivel_tanque(env, tanque)
