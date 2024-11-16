from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    def establecerNombre(self, nombre):
        self.__nombre = nombre

    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    def __eq__(self, other):
        if isinstance(other, EntidadVineria):
            return self.obtenerId() == other.obtenerId()
        return False

    def __hash__(self):
        return hash(self.obtenerId())