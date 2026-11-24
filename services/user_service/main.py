
from fastapi import FastAPI
from services.user_service.metrics import obtener_cpu
import threading
import time
from prometheus_client import Gauge, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI(title="Users Service")

cpu_gauge = Gauge(
    "service_cpu_usage_percent",
    "Uso de CPU del microservicio",
    ["service"]
)

@app.get("/")
def inicio():
    return {
        "servicio": "Users Service",
        "estado": "activo"
    }


@app.get("/users")
def obtener_usuarios():
    return {
        "usuarios": [
            {"id": 1, "nombre": "Ana"},
            {"id": 2, "nombre": "Carlos"}
        ]
    }

@app.get("/metrics/cpu")
def consultar_cpu():
    return {
        "servicio": "Users Service",
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

@app.get("/metrics")
def metricas_prometheus():

    cpu = obtener_cpu()

    cpu_gauge.labels(service="user_service").set(cpu)

    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
