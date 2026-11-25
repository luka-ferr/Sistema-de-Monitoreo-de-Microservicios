from adapters.prometheus_adapter import PrometheusAdapter
from adapters.legacy_api_adapter import LegacyAPIAdapter
from observers.subject import Subject
from observers.email_alert import EmailAlert
from observers.slack_alert import SlackAlert

adapter = LegacyAPIAdapter()
adapter1 = PrometheusAdapter("user_service")
adapter2 = PrometheusAdapter("payments_service")

monitor = Subject()
email = EmailAlert()
slack = SlackAlert()

monitor.attach(email)
monitor.attach(slack)

cpu1 = adapter1.get_cpu_usage()
cpu2 = adapter2.get_cpu_usage()

print("Uso de CPU del servicio de usuarios:", cpu1, "%")
print("Uso de CPU del servicio de pagos:", cpu2, "%")


cpu = adapter.get_cpu_usage()

print("Uso de CPU del servicio orders:", cpu, "%")

monitor.notify("user_service", 85)