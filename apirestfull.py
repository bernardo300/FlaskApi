from flask import Flask, request
import json
from flask_restful import Resource, Api

from habilidade import Habilidade

app = Flask(__name__)
api = Api(app)

desenvolvedores = [{'nome': 'Kennedy', 'hablidade': ['java', 'python']},
                   {'nome': 'Gabriel', 'hablidade': ['kotlin', 'android']}]


class Desenvolvedor(Resource):
    def get(self):
        return desenvolvedores

    def put(self):
        dev = json.loads(request.data)
        id = int(dev['id'])
        try:
            desenvolvedores[id] = dev
        except:
            dev = {'error', 'erro ao editar'}
        return dev

    def delete(self):
        id = int(json.loads(request.data)['id'])
        msg = {'msg': 'sucesso'}
        try:
            desenvolvedores.pop(id)
        except:
            msg = {'msg', 'error'}
        return msg

    def post(self):
        dev = json.loads(request.data)
        desenvolvedores.append(dev)
        return dev


api.add_resource(Desenvolvedor, '/dev')
api.add_resource(Habilidade, '/hab')

if __name__ == '__main__':
    app.run(debug=True)
c
