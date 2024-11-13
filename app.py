# Flask
from flask import Flask
from flask_restful import Api
import json

#from vinoteca import Vinoteca

#from modelos.bodega import Bodega
#from modelos.cepa import Cepa
#from modelos.vino import Vino

# API
#from recursos import *

app = Flask(__name__)
api = Api(app)

#api.add_resource(RecursoBodega, '/api/bodegas/<id>')
#api.add_resource(RecursoBodegas, '/api/bodegas')
#api.add_resource(RecursoCepa, '/api/cepas/<id>')
#api.add_resource(RecursoCepas, '/api/cepas')
#api.add_resource(RecursoVino, '/api/vinos/<id>')
#api.add_resource(RecursoVinos, '/api/vinos')


@app.route("/", methods=["GET"])
def index():
    with open('vinoteca.json') as file:
        data = dict(json.load(file))
        return data
########### todos arriba
@app.route("/api/bodegas", methods=["GET"])
def bodegas():
    with open('vinoteca.json') as file:
        data = dict(json.load(file))
        for key, value in data.items():
            if key == list(data.keys())[0]:
                return value

@app.route("/api/cepas", methods=["GET"])
def cepas():
    with open('vinoteca.json') as file:
        data = dict(json.load(file))
        for key, value in data.items():
            if key == list(data.keys())[1]: # aca solo el numero se cambia
                return value 

@app.route("/api/vinos", methods=["GET"])
def vinos():
    with open('vinoteca.json') as file:
        data = dict(json.load(file))
        for key, value in data.items():
            if key == list(data.keys())[2]:
                return value
############3 bodegas, cepas y vinos x separado arriba

@app.route("/api/bodegas/<string:id>", methods=["GET"])
def get_bodega(id):
    todas_las_bodegas = bodegas()
    for bodega in todas_las_bodegas:
        if bodega["id"] == id:
            return bodega



if __name__ == "__main__":
    app.run(debug=True)

