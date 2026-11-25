import time

from config.monitoring_config import MonitoringConfig
from observers.subject import Subject

from adapters.prometheus_adapter import PrometheusAdapter
from adapters.legacy_api_adapter import LegacyAPIAdapter


class MonitoringFacade:

    def __init__(self):

        self.config = MonitoringConfig()

        self.subject = Subject()

        self.services = {}

    def register_service(self, service_name, adapter):

        self.services[service_name] = adapter

        print(f"Servicio registrado: {service_name}")

    def monitor_service(self, service_name, adapter):

        cpu_usage = adapter.get_cpu_usage()

        threshold = self.config.cpu_threshold

        print(
            f"{service_name}: {cpu_usage:.2f}% CPU "
            f"(Umbral: {threshold}%)"
        )

        if cpu_usage > threshold:

            print(f"¡ALERTA! {service_name} superó el umbral.")

            self.subject.notify(service_name, cpu_usage)

    def monitor_all(self):

        for service_name, adapter in self.services.items():

            try:
                self.monitor_service(service_name, adapter)

            except Exception as error:
                print(f"Error monitoreando {service_name}: {error}")

    def start_monitoring(self, interval=10):

        print("\nIniciando sistema de monitoreo...\n")

        while True:

            print("\n========== CICLO DE MONITOREO ==========")

            self.monitor_all()

            print("\nPróxima revisión en", interval, "segundos")

            time.sleep(interval)