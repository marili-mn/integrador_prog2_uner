# Proyecto Vinoteca Virtual - API con Flask

Este proyecto consiste en desarrollar una API para una vinoteca virtual que expone datos sobre bodegas, cepas y vinos. La API utiliza un archivo JSON (`vinoteca.json`) como base de datos.

## Estructura de Datos JSON

El archivo JSON `vinoteca.json` tiene la siguiente estructura para representar las relaciones entre bodegas, cepas y vinos:

```json
{
  "bodegas": [
    {
      "id": "b1",
      "nombre": "Casa La Primavera Bodegas y Viñedos",
      "cepas": ["c1", "c2", "c3"],
      "vinos": ["v1", "v2"]
    },
    {
      "id": "b2",
      "nombre": "Bodega Sottano",
      "cepas": ["c2", "c4"],
      "vinos": ["v3"]
    }
  ],
  "cepas": [
    {
      "id": "c1",
      "nombre": "Chardonnay",
      "vinos": ["v1"]
    },
    {
      "id": "c2",
      "nombre": "Malbec",
      "vinos": ["v1", "v2", "v3"]
    },
    {
      "id": "c3",
      "nombre": "Cabernet Sauvignon",
      "vinos": ["v2"]
    },
    {
      "id": "c4",
      "nombre": "Merlot",
      "vinos": ["v3"]
    }
  ],
  "vinos": [
    {
      "id": "v1",
      "nombre": "Prófugo",
      "bodega": "b1",
      "cepas": ["c1", "c2"],
      "partidas": [2023, 2024]
    },
    {
      "id": "v2",
      "nombre": "Oveja Black",
      "bodega": "b1",
      "cepas": ["c2", "c3"],
      "partidas": [2022, 2023]
    },
    {
      "id": "v3",
      "nombre": "Sottano",
      "bodega": "b2",
      "cepas": ["c2", "c4"],
      "partidas": [2021, 2022]
    }
  ]
}

Estructura del Proyecto

Organiza el proyecto según la siguiente estructura de archivos:

bash

vinoteca_api/
├── app.py                # Archivo principal de la aplicación Flask
├── vinoteca.json         # Base de datos en formato JSON
├── models/
│   ├── entidadvineria.py # Clase base abstracta para Bodega, Cepa y Vino
│   ├── bodega.py         # Clase Bodega
│   ├── cepa.py           # Clase Cepa
│   └── vino.py           # Clase Vino
└── controllers/
    ├── vinoteca.py       # Controlador principal para manejar las consultas

Implementación de app.py

Este archivo define las rutas de la API para obtener datos sobre bodegas, cepas y vinos:

python

from flask import Flask, jsonify, request
from controllers.vinoteca import Vinoteca

app = Flask(__name__)

# Rutas para los servicios
@app.route('/api/bodegas', methods=['GET'])
def get_bodegas():
    orden = request.args.get('orden')
    reverso = request.args.get('reverso', 'no') == 'si'
    bodegas = Vinoteca.obtener_bodegas(orden, reverso)
    return jsonify(bodegas)

@app.route('/api/bodegas/<id>', methods=['GET'])
def get_bodega(id):
    bodega = Vinoteca.buscar_bodega(id)
    return jsonify(bodega) if bodega else jsonify({"error": "Bodega no encontrada"}), 404

# Puedes añadir rutas similares para cepas y vinos aquí

if __name__ == '__main__':
    app.run(debug=True)

Implementación de Vinoteca en controllers/vinoteca.py

Esta clase maneja la lógica de negocio y la interacción con el archivo JSON:

python

import json
from models.bodega import Bodega
from models.cepa import Cepa
from models.vino import Vino

class Vinoteca:
    archivo_datos = "vinoteca.json"
    bodegas = []
    cepas = []
    vinos = []

    @classmethod
    def inicializar(cls):
        with open(cls.archivo_datos, 'r') as archivo:
            datos = json.load(archivo)
            cls.bodegas = [Bodega(**b) for b in datos.get("bodegas", [])]
            cls.cepas = [Cepa(**c) for c in datos.get("cepas", [])]
            cls.vinos = [Vino(**v) for v in datos.get("vinos", [])]

    @classmethod
    def obtener_bodegas(cls, orden=None, reverso=False):
        bodegas = cls.bodegas
        if orden:
            bodegas = sorted(bodegas, key=lambda b: getattr(b, orden), reverse=reverso)
        return [bodega.convertir_a_json() for bodega in bodegas]

    @classmethod
    def buscar_bodega(cls, id):
        for bodega in cls.bodegas:
            if bodega.id == id:
                return bodega.convertir_a_json()
        return None

Sugerencias para Mejoras Legacy

    Modularidad Extrema: Implementa cada método de forma aislada para facilitar la modificación y prueba de cada uno.
    Manejadores de Errores (try-except): Agrega bloques try-except para capturar y manejar errores de forma controlada en cada servicio.
    Abstracción de Métodos Comunes: Define métodos compartidos en la clase base EntidadVineria para evitar redundancia entre Bodega, Cepa, y Vino.
    Uso de Decoradores: Usa decoradores para añadir funcionalidades adicionales, como autenticación, validación y registro de accesos.
    Pruebas Unitarias y de Integración: Escribe pruebas para verificar que las rutas y consultas de la API funcionan según lo esperado.

Con esta estructura inicial y las buenas prácticas mencionadas, tendrás un proyecto organizado y fácil de escalar.