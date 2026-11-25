import requests
from adapters.interface import MonitoringAdapter


class LegacyAPIAdapter(MonitoringAdapter):

    def __init__(self):
        self.api_url = "http://localhost:8003/metrics/cpu"

    def get_cpu_usage(self):

        response = requests.get(self.api_url, timeout=5)

        response.raise_for_status()

        datos = response.json()

        cpu = float(datos["cpu_usage_percent"])

        return cpu