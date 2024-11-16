from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __eq__(self, other):
        return self.id == other.id

    def obtenerId(self):
        return self.id

    def obtenerNombre(self):
        return self.nombre

    def establecerNombre(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def convertirAJSON(self):
        pass
