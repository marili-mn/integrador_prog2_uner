import os
import json
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    @classmethod
    def inicializar(cls):
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(datos)

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        bodegas = cls.__bodegas
        if orden == "nombre":
            bodegas = sorted(bodegas, key=lambda b: b.obtenerNombre(), reverse=reverso)
        elif orden == "vinos":
            bodegas = sorted(bodegas, key=lambda b: len(b.obtenerVinos()), reverse=reverso)
        return bodegas

    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        cepas = cls.__cepas
        if orden == "nombre":
            cepas = sorted(cepas, key=lambda c: c.obtenerNombre(), reverse=reverso)
        return cepas

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos = cls.__vinos
        if anio:
            vinos = [v for v in vinos if anio in v.obtenerPartidas()]
        if orden == "nombre":
            vinos = sorted(vinos, key=lambda v: v.obtenerNombre(), reverse=reverso)
        elif orden == "bodega":
            vinos = sorted(vinos, key=lambda v: v.obtenerBodega().obtenerNombre(), reverse=reverso)
        elif orden == "cepas":
            vinos = sorted(vinos, key=lambda v: [c.obtenerNombre() for c in v.obtenerCepas()], reverse=reverso)
        return vinos

    @classmethod
    def buscarBodega(cls, id):
        for bodega in cls.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None

    @classmethod
    def buscarCepa(cls, id):
        for cepa in cls.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None

    @classmethod
    def buscarVino(cls, id):
        for vino in cls.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None

    @classmethod
    def __parsearArchivoDeDatos(cls):
        with open(cls.__archivoDeDatos, 'r') as archivo:
            return json.load(archivo)

    @classmethod
    def __convertirJsonAListas(cls, datos):
        cls.__bodegas = [Bodega(b['id'], b['nombre']) for b in datos['bodegas']]
        cls.__cepas = [Cepa(c['id'], c['nombre']) for c in datos['cepas']]
        cls.__vinos = [Vino(v['id'], v['nombre'], v['bodega'], v['cepas'], v['partidas']) for v in datos['vinos']]