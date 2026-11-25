# Sistema-de-Monitoreo-de-Microservicios.
Trabajo académico (UTP): sistema de monitoreo de microservicios en Python aplicando los patrones de diseño Singleton, Observer, Adapter y Facade, con arquitectura en capas.

Comandos para correr cada servicio:
ejecutar cada uno en una terminal diferente

source .venv/Scripts/activate
uvicorn services.user_service.main:app --reload --port 8001

source .venv/Scripts/activate
uvicorn services.payments_service.main:app --reload --port 8002

source .venv/Scripts/activate
uvicorn services.orders_service.main:app --reload --port 8003