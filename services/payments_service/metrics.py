
import psutil
import os


# Obtener el proceso actual del microservicio
proceso = psutil.Process(os.getpid())

# Obtener el proceso actual del microservicio
proceso.cpu_percent(interval=None)


def obtener_cpu():
    return proceso.cpu_percent(interval=None)