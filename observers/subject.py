class Subject:

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, service_name, cpu_usage):

        for observer in self.observers:
            observer.update(service_name, cpu_usage)