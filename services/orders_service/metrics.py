import psutil
import os

proceso = psutil.Process(os.getpid())

proceso.cpu_percent(interval=None)


def obtener_cpu():
    return proceso.cpu_percent(interval=None)