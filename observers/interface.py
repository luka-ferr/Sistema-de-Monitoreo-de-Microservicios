from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, service_name, cpu_usage):
        pass