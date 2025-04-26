import simpy

VELOCIDAD_TANQUEO = 2  # Litros por segundo


def crear_recursos(env, surtidores_cantidad=2, tanque_capacidad=20000):
    surtidores = simpy.Resource(env, capacity=surtidores_cantidad)
    tanque = simpy.Container(env, init=tanque_capacidad, capacity=tanque_capacidad)

    recursos = {
        'surtidores': surtidores,
        'tanque': tanque,
    }
    return recursos