from flask import Flask, jsonify, request
import json
app = Flask(__name__)
desenvolvedores = [{'nome': 'Kennedy', 'hablidade': ['java', 'python']},
                   {'nome': 'Gabriel', 'hablidade': ['kotlin', 'android']}]


@app.route('/api', methods=['GET'])
def getAll():
    return jsonify(desenvolvedores)


@app.route('/api/<int:id>', methods=['GET'])
def getOne(id):
    try:
        dev = desenvolvedores[id]
    except:
        dev = {'error': 'id nao encontrado'}
    return jsonify(dev)


@app.route('/api', methods=['DELETE'])
def delete():
    id = int(json.loads(request.data)['id'])
    msg = {'msg': 'sucesso'}
    try:
        desenvolvedores.pop(id)
    except:
        msg = {'msg', 'error'}
    return jsonify(msg)


@app.route('/api', methods=['POST'])
def create():
    dev = json.loads(request.data)
    desenvolvedores.append(dev)
    return jsonify(dev)


@app.route('/api', methods=['PUT'])
def editar():
    dev = json.loads(request.data)
    id = int(dev['id'])
    try:
        desenvolvedores[id] = dev
    except:
        dev = {'error', 'erro ao editar'}
    return jsonify(dev)


if __name__ == '__main__':
    app.run(debug=True)
