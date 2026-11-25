
import requests
from adapters.interface import MonitoringAdapter


class PrometheusAdapter(MonitoringAdapter):

    def __init__(self, service_name):
        self.service_name = service_name
        self.prometheus_url = "http://localhost:9090"

    def get_cpu_usage(self):

        url = f"{self.prometheus_url}/api/v1/query"

        params = {
            "query": f'service_cpu_usage_percent{{service="{self.service_name}"}}'
        }

        response = requests.get(url, params=params, timeout=5)

        response.raise_for_status()

        datos = response.json()

        resultados = datos["data"]["result"]

        if not resultados:
            raise ValueError(
                f"No se encontraron métricas para {self.service_name}"
            )

        cpu = float(resultados[0]["value"][1])

        return cpu
