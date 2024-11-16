import json
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

class Vinoteca:
    archivoDeDatos = "vinoteca.json"
    bodegas = []
    cepas = []
    vinos = []

    @classmethod
    def inicializar(cls):
        data = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(data)

    @classmethod
    def __parsearArchivoDeDatos(cls):
        with open(cls.archivoDeDatos, 'r', encoding='utf-8') as f:
            return json.load(f)

    @classmethod
    def __convertirJsonAListas(cls, data):
        cls.bodegas = [Bodega(**b) for b in data['bodegas']]
        cls.cepas = [Cepa(**c) for c in data['cepas']]
        cls.vinos = [Vino(**v) for v in data['vinos']]

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        return sorted(cls.bodegas, key=lambda b: getattr(b, orden), reverse=reverso) if orden else cls.bodegas

    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        return sorted(cls.cepas, key=lambda c: getattr(c, orden), reverse=reverso) if orden else cls.cepas

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos = cls.vinos
        if anio:
            vinos = [v for v in vinos if anio in v.partidas]
        return sorted(vinos, key=lambda v: getattr(v, orden), reverse=reverso) if orden else vinos

    @classmethod
    def obtenerVinosDeBodega(cls, bodega_id):
        return [v for v in cls.vinos if v.bodega == bodega_id]

    @classmethod
    def obtenerCepasDeBodega(cls, bodega_id):
        vinos = cls.obtenerVinosDeBodega(bodega_id)
        cepas = set()
        for vino in vinos:
            cepas.update(vino.cepas)
        return [cls.buscarCepa(cepa_id) for cepa_id in cepas]

    @classmethod
    def obtenerVinosPorCepa(cls, cepa_id):
        return [v for v in cls.vinos if cepa_id in v.cepas]

    @classmethod
    def obtenerCepasDeVino(cls, cepas_ids):
        return [cls.buscarCepa(id) for id in cepas_ids]

    @classmethod
    def buscarBodega(cls, id):
        return next((b for b in cls.bodegas if b.id == id), None)

    @classmethod
    def buscarCepa(cls, id):
        return next((c for c in cls.cepas if c.id == id), None)

    @classmethod
    def buscarVino(cls, id):
        return next((v for v in cls.vinos if v.id == id), None)
