from entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def convertirAJSON(self):
        return {"id": self.id, "nombre": self.nombre}

    def convertirAJSONFull(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cepas": [c.obtenerNombre() for c in self.obtenerCepas()],
            "vinos": [v.obtenerNombre() for v in self.obtenerVinos()]
        }

    def obtenerVinos(self):
        from vinoteca import Vinoteca  # Importación diferida
        return Vinoteca.obtenerVinosDeBodega(self.id)

    def obtenerCepas(self):
        from vinoteca import Vinoteca  # Importación diferida
        return Vinoteca.obtenerCepasDeBodega(self.id)
