from observers.interface import Observer


class SlackAlert(Observer):

    def update(self, service_name, cpu_usage):

        print("\n========== ALERTA POR SLACK ===========")

        print(f"Servicio: {service_name}")
        print(f"Uso de CPU: {cpu_usage}%")
        print("Mensaje: El consumo de CPU superó el umbral permitido.")

        print("=======================================\n")