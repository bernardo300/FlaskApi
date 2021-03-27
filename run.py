from flask import Flask, jsonify, request
import json
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'nome': 'Kennedy'})


@app.route('/soma/<int:a>/<int:b>', methods=['GET'])
def soma(a, b):
    total = a + b
    return jsonify({'total': str(total)})


@app.route('/soma', methods=['POST', 'GET'])
def soma2():
    if request.method == 'POST':
        data = json.loads(request.data)
        soma = sum(data['dados'])
        return jsonify({'total': soma})
    elif request.method == 'GET':
        return jsonify({'total': 45})


if __name__ == '__main__':
    app.run(debug=True)
