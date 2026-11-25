
class MonitoringConfig:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.cpu_threshold = 80
            self._initialized = True
