# Sistema de Monitoreo de Microservicios

**Trabajo académico – Universidad Tecnológica de Pereira (UTP)**

Sistema de monitoreo de microservicios desarrollado en Python con FastAPI, aplicando los patrones de diseño Singleton, Observer, Adapter y Facade, mediante una arquitectura organizada por capas.

## 1. Objetivo del proyecto

Desarrollar un sistema centralizado que permita monitorear el consumo de CPU de diferentes microservicios, identificar cuándo se supera un umbral establecido y generar alertas mediante distintos mecanismos de notificación.

El sistema implementa cuatro patrones de diseño:

- **Singleton:** garantiza una única instancia de configuración centralizada.
- **Observer:** permite notificar a diferentes mecanismos de alerta cuando se supera el umbral.
- **Adapter:** normaliza la obtención de métricas provenientes de distintas API.
- **Facade:** proporciona una interfaz sencilla para coordinar el proceso de monitoreo.

## 2. Arquitectura del sistema

El proyecto está compuesto por tres microservicios independientes y un sistema central de monitoreo.

| Componente | Puerto | Fuente de métricas |
|---|---:|---|
| User Service | 8001 | Prometheus |
| Payments Service | 8002 | Prometheus |
| Orders Service | 8003 | API legada simulada |

Prometheus recopila las métricas de User Service y Payments Service. Para Orders Service se utiliza directamente su endpoint `/metrics/cpu`, que devuelve los datos en formato JSON.

El sistema central consulta ambas fuentes mediante los adaptadores correspondientes.

## 3. Estructura del proyecto

```text
Sistema-de-Monitoreo/
│
├── adapters/
│   ├── __init__.py
│   ├── interface.py
│   ├── prometheus_adapter.py
│   └── legacy_api_adapter.py
│
├── config/
│   ├── __init__.py
│   └── monitoring_config.py
│
├── facade/
│   ├── __init__.py
│   └── monitoring_facade.py
│
├── observers/
│   ├── __init__.py
│   ├── interface.py
│   ├── subject.py
│   ├── email_alert.py
│   └── slack_alert.py
│
├── services/
│   ├── user_service/
│   ├── payments_service/
│   └── orders_service/
│
├── tests/
│
├── .venv/
├── main.py
└── requirements.txt
```

## 4. Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- Prometheus
- Prometheus Client
- psutil
- Requests

## 5. Requisitos previos

Antes de ejecutar el proyecto, se debe contar con:

- Python instalado.
- Visual Studio Code.
- Prometheus descargado y configurado.
- Git Bash o una terminal compatible.

## 6. Preparación del entorno

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta:

```bash
cd Sistema-de-Monitoreo
```

Crear el entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual desde Git Bash:

```bash
source .venv/Scripts/activate
```

### Instalación de dependencias

El proyecto incluye un archivo `requirements.txt` con las librerías necesarias para su funcionamiento.

Contenido del archivo:

```text
fastapi
uvicorn
psutil
prometheus-client
requests
```

Para instalar todas las dependencias, ejecutar:

```bash
pip install -r requirements.txt
```

De esta manera, no es necesario instalar cada librería individualmente.

## 7. Configuración de Prometheus

Prometheus se utiliza para recopilar las métricas de CPU de User Service y Payments Service.

Dentro de la carpeta de Prometheus, crear o modificar el archivo `prometheus.yml`:

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: "microservicios"
    static_configs:
      - targets:
          - "localhost:8001"
          - "localhost:8002"
```

Se configuran únicamente estos dos servicios porque Orders Service utiliza el adaptador de API legada.

### Ejecutar Prometheus

Desde la carpeta donde se encuentra el ejecutable de Prometheus:

```bash
./prometheus.exe --config.file=prometheus.yml
```

Interfaz web de Prometheus:

http://localhost:9090

Estado de los servicios monitoreados:

http://localhost:9090/targets

## 8. Ejecución de los microservicios

Cada microservicio debe ejecutarse en una terminal independiente.

### User Service

```bash
source .venv/Scripts/activate
uvicorn services.user_service.main:app --reload --port 8001
```

### Payments Service

```bash
source .venv/Scripts/activate
uvicorn services.payments_service.main:app --reload --port 8002
```

### Orders Service

```bash
source .venv/Scripts/activate
uvicorn services.orders_service.main:app --reload --port 8003
```

## 9. Endpoints disponibles

Los microservicios exponen endpoints para consultar su estado y obtener métricas.

| Endpoint | Función |
|---|---|
| `/` | Consultar el estado del servicio. |
| `/metrics/cpu` | Obtener el consumo de CPU en formato JSON. |
| `/test/cpu` | Generar carga de CPU para realizar pruebas. |
| `/metrics` | Exponer métricas en formato compatible con Prometheus, cuando está implementado en el servicio. |

Para consultar las métricas de Orders Service:

http://localhost:8003/metrics/cpu

## 10. Ejecución del sistema central de monitoreo

Una vez que Prometheus y los tres microservicios estén ejecutándose, abrir una nueva terminal en la raíz del proyecto.

Activar el entorno virtual:

```bash
source .venv/Scripts/activate
```

Ejecutar el sistema central:

```bash
python main.py
```

El sistema registrará los tres microservicios y comenzará a consultar periódicamente sus métricas de CPU.

Cuando un servicio supere el umbral configurado del 80 %, se generarán las notificaciones correspondientes.

## 11. Patrones de diseño implementados

### Singleton

Implementado mediante la clase `MonitoringConfig`, que centraliza la configuración del sistema y permite compartir el umbral de CPU entre los componentes del monitor.

### Observer

Implementado mediante `Subject`, `EmailAlert` y `SlackAlert`.

Permite registrar diferentes observadores y notificarles cuando se supera el umbral de CPU.

Las notificaciones de correo y Slack se simulan mediante mensajes en consola; no realizan envíos reales.

### Adapter

Implementado mediante dos adaptadores:

- `PrometheusAdapter`: consulta las métricas de User Service y Payments Service.
- `LegacyAPIAdapter`: consulta el endpoint JSON de Orders Service.

Ambos implementan la interfaz `MonitoringAdapter` y exponen el método `get_cpu_usage()`, permitiendo que el sistema central obtenga las métricas de manera uniforme.

### Facade

Implementado mediante `MonitoringFacade`, que simplifica la interacción con los componentes del sistema.

Se encarga de registrar servicios, obtener métricas, comparar el consumo de CPU con el umbral y activar las notificaciones correspondientes.

## 12. Consideraciones

- Los tres microservicios se ejecutan de manera independiente.
- Prometheus recopila las métricas de User Service y Payments Service.
- Orders Service proporciona sus métricas mediante una API legada simulada.
- El umbral de CPU se encuentra centralizado en `MonitoringConfig`.
- Las alertas se generan cuando el consumo de CPU supera el 80 %.
- Las notificaciones por correo y Slack son simulaciones en consola.

## 13. Resultado esperado

Al ejecutar `main.py`, el sistema debe registrar los tres microservicios y realizar ciclos periódicos de monitoreo.

En cada ciclo se consulta el consumo de CPU, se compara con el umbral establecido y, cuando corresponde, se notifican las alertas mediante los observadores registrados.

El proyecto demuestra cómo integrar diferentes fuentes de métricas y aplicar patrones de diseño para construir un sistema de monitoreo modular y extensible.