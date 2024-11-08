import json
from entidadvineria import EntidadVineria

class Bodega:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    def abrirJson(self):        #metodo auxiliar
        with open('vinoteca.json') as file:
            data = json.load(file)
            return data

    def salidaBodega(self, id):
        data = self.abrirJson(self)
        bodegas = data['vinos']
        bodegas_sin_partidas = bodegas.partidas.pop()
        return bodegas_sin_partidas
    
        
        


    def obtenerVinos(self):







"""
class Bodega:

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "id": EntidadVineria.obtenerId(),
            "nombre": EntidadVineria.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)
"""