
from abc import ABC, abstractmethod


class MonitoringAdapter(ABC):

    @abstractmethod
    def get_cpu_usage(self):
        pass
