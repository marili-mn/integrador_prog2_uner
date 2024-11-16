from entidadvineria import EntidadVineria

class Cepa(EntidadVineria):
    def convertirAJSON(self):
        return {"id": self.id, "nombre": self.nombre}

    def convertirAJSONFull(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "vinos": [f"{v.obtenerNombre()} ({v.obtenerBodega().obtenerNombre()})" for v in self.obtenerVinos()]
        }

    def obtenerVinos(self):
        from vinoteca import Vinoteca  # Importación diferida
        return Vinoteca.obtenerVinosPorCepa(self.id)
