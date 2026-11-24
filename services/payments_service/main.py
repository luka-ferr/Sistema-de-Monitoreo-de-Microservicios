
from fastapi import FastAPI
from services.payments_service.metrics import obtener_cpu
import threading
import time

app = FastAPI(title="Payments Service")


@app.get("/")
def inicio():
    return {
        "servicio": "Payments Service",
        "estado": "activo"
    }


@app.get("/payments")
def obtener_pagos():
    return {
        "pagos": [
            {"id": 1, "usuario": "Ana", "valor": 50000},
            {"id": 2, "usuario": "Carlos", "valor": 75000}
        ]
    }


@app.get("/metrics/cpu")
def consultar_cpu():
    return {
        "servicio": "Payments Service",
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
