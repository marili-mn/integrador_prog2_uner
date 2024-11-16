from .entidadvineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id, nombre, bodega, cepas, partidas):
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas

    def establecerBodega(self, bodega):
        self.__bodega = bodega

    def establecerCepas(self, cepas):
        self.__cepas = cepas

    def establecerPartidas(self, partidas):
        self.__partidas = partidas

    def obtenerBodega(self):
        from vinoteca import Vinoteca
        return Vinoteca.buscarBodega(self.__bodega)

    def obtenerCepas(self):
        from vinoteca import Vinoteca
        return [Vinoteca.buscarCepa(cepa_id) for cepa_id in self.__cepas]

    def obtenerPartidas(self):
        return self.__partidas

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": [cepa.obtenerNombre() for cepa in self.obtenerCepas()],
            "partidas": self.obtenerPartidas()
        }

    def convertirAJSONFull(self):
        return self.convertirAJSON()