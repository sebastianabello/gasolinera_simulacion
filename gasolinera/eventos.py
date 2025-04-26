nivel_tanque_log = []
clientes_atendidos = 0
clientes_rechazados = 0

def registrar_nivel_tanque(env, tanque):
    """
    Registra el nivel actual del tanque en el tiempo.
    """
    nivel_tanque_log.append((env.now, tanque.level))

def registrar_cliente(atendido):
    """
    Registra si un cliente fue atendido (True) o rechazado (False).
    """
    global clientes_atendidos, clientes_rechazados
    if atendido:
        clientes_atendidos += 1
    else:
        clientes_rechazados += 1

def reset_eventos():
    """
    Resetea los registros de eventos para una nueva simulación.
    """
    global nivel_tanque_log, clientes_atendidos, clientes_rechazados
    nivel_tanque_log.clear()
    clientes_atendidos = 0
    clientes_rechazados = 0