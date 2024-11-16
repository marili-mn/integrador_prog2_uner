from flask import Flask, jsonify, request
from vinoteca import Vinoteca

app = Flask(__name__)

Vinoteca.inicializar()

@app.route('/api/bodegas/<id>', methods=['GET'])
def obtener_bodega(id):
    bodega = Vinoteca.buscarBodega(id)
    if bodega:
        return jsonify(bodega.convertirAJSONFull())
    return jsonify({"error": "Bodega no encontrada"}), 404

@app.route('/api/bodegas', methods=['GET'])
def listar_bodegas():
    orden = request.args.get('orden')
    reverso = request.args.get('reverso') == "si"
    bodegas = Vinoteca.obtenerBodegas(orden, reverso)
    return jsonify([b.convertirAJSON() for b in bodegas])

@app.route('/api/cepas/<id>', methods=['GET'])
def obtener_cepa(id):
    cepa = Vinoteca.buscarCepa(id)
    if cepa:
        return jsonify(cepa.convertirAJSONFull())
    return jsonify({"error": "Cepa no encontrada"}), 404

@app.route('/api/cepas', methods=['GET'])
def listar_cepas():
    orden = request.args.get('orden')
    reverso = request.args.get('reverso') == "si"
    cepas = Vinoteca.obtenerCepas(orden, reverso)
    return jsonify([c.convertirAJSON() for c in cepas])

@app.route('/api/vinos/<id>', methods=['GET'])
def obtener_vino(id):
    vino = Vinoteca.buscarVino(id)
    if vino:
        return jsonify(vino.convertirAJSONFull())
    return jsonify({"error": "Vino no encontrado"}), 404

@app.route('/api/vinos', methods=['GET'])
def listar_vinos():
    orden = request.args.get('orden')
    reverso = request.args.get('reverso') == "si"
    anio = request.args.get('anio')
    anio = int(anio) if anio else None
    vinos = Vinoteca.obtenerVinos(anio, orden, reverso)
    return jsonify([v.convertirAJSON() for v in vinos])

if __name__ == '__main__':
    app.run(debug=True)
