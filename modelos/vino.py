from entidadvineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id, nombre, bodega, cepas, partidas):
        super().__init__(id, nombre)
        self.bodega = bodega
        self.cepas = cepas
        self.partidas = partidas

    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": [c.obtenerNombre() for c in self.obtenerCepas()],
            "partidas": self.partidas
        }

    def convertirAJSONFull(self):
        return self.convertirAJSON()

    def obtenerBodega(self):
        from vinoteca import Vinoteca  # Importación diferida
        return Vinoteca.buscarBodega(self.bodega)

    def obtenerCepas(self):
        from vinoteca import Vinoteca  # Importación diferida
        return Vinoteca.obtenerCepasDeVino(self.cepas)