
from fastapi import FastAPI
from services.orders_service.metrics import obtener_cpu
import threading
import time

app = FastAPI(title="Orders Service")


@app.get("/")
def inicio():
    return {
        "servicio": "Orders Service",
        "estado": "activo"
    }


@app.get("/orders")
def obtener_pedidos():
    return {
        "pedidos": [
            {"id": 1, "producto": "Computador", "cantidad": 2},
            {"id": 2, "producto": "Teclado", "cantidad": 5}
        ]
    }


@app.get("/metrics/cpu")
def consultar_cpu():
    return {
        "servicio": "Orders Service",
        "cpu_usage_percent": obtener_cpu()
    }


def generar_carga_cpu():
    fin = time.time() + 30

    while time.time() < fin:
        resultado = 0
        for numero in range(100000):
            resultado += numero * numero


@app.get("/test/cpu")
def probar_cpu():
    hilo = threading.Thread(target=generar_carga_cpu)
    hilo.start()

    return {
        "mensaje": "Carga de CPU iniciada",
        "duracion_segundos": 30
    }
