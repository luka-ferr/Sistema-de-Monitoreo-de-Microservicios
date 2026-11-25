from facade.monitoring_facade import MonitoringFacade

from adapters.prometheus_adapter import PrometheusAdapter
from adapters.legacy_api_adapter import LegacyAPIAdapter

from observers.email_alert import EmailAlert
from observers.slack_alert import SlackAlert


# Crear la fachada
monitoring = MonitoringFacade()


# Registrar observadores
monitoring.subject.attach(EmailAlert())
monitoring.subject.attach(SlackAlert())


# Registrar microservicios
monitoring.register_service(
    "user_service",
    PrometheusAdapter("user_service")
)

monitoring.register_service(
    "payments_service",
    PrometheusAdapter("payments_service")
)

monitoring.register_service(
    "orders_service",
    LegacyAPIAdapter()
)


# Iniciar monitoreo periódico
monitoring.start_monitoring(interval=10)