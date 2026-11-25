from adapters.prometheus_adapter import PrometheusAdapter
from adapters.legacy_api_adapter import LegacyAPIAdapter

adapter = LegacyAPIAdapter()
adapter1 = PrometheusAdapter("user_service")
adapter2 = PrometheusAdapter("payments_service")

cpu1 = adapter1.get_cpu_usage()
cpu2 = adapter2.get_cpu_usage()

print("Uso de CPU del servicio de usuarios:", cpu1, "%")
print("Uso de CPU del servicio de pagos:", cpu2, "%")


cpu = adapter.get_cpu_usage()

print("Uso de CPU del servicio orders:", cpu, "%")