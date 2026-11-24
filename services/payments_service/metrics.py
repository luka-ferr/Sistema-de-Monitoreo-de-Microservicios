
import psutil
import os

# Obtener el proceso actual del microservicio
proceso = psutil.Process(os.getpid())


def obtener_cpu():
    return proceso.cpu_percent(interval=10)
