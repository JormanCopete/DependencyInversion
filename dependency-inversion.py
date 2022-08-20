from abc import ABC, abstractmethod

class Conmutable(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class Bombillo(Conmutable):
    def encender(self):
        print("Bombillo: Encendido")

    def apagar(self):
        print("Bombillo: Apagado")

class Fan(Conmutable):
    def encender(self):
        print("Ventilador: Encendido")

    def apagar(self):
        print("Ventilador: Apagado")

class InterructorElectrico:
    def __init__(self, c: Conmutable):
        self.client = c
        self.on = False

    def presionar(self):
        if self.on:
            self.client.apagar()
            self.on = False
        else:
            self.client.encender()
            self.on = True

l = Bombillo()
f = Fan()
switch = InterructorElectrico(l)
switch.presionar()
switch.presionar()