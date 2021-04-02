from flask import Flask, request
import json
from flask_restful import Resource, Api

from habilidade import Habilidade
from models import Pessoa, Atividade, Usuario

from flask_httpauth import HTTPBasicAuth


USUARIOS = {
    'kennedy': '123',
    'gabriel': '123'
}

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuario.query.filter_by(login=login, senha=senha).first()


class Dado(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        try:
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade,
            }
            return response
        except AttributeError:
            return {'msg': 'Nao encontrado'}

    def put(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()

        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        res = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return res

    def delete(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        pessoa.delete()
        return {'msg': 'deletado'}


class ListaDados(Resource):
    def get(self):
        pessoas = Pessoa.query.all()
        response = [{'id': p.id, 'nome': p.nome, 'idade': p.idade}
                    for p in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoa(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        res = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return res


class Atv(Resource):
    def post(self):
        dados = request.json
        pessoa = Pessoa.query.filter_by(nome=dados['pessoa']).first()
        atv = Atividade(nome=dados['nome'], pessoa=pessoa)
        atv.save()
        res = {
            'id': atv.id,
            'nome': atv.nome,
            'pessoa': atv.pessoa.nome
        }
        return res

    def get(self):
        pessoas = Atividade.query.all()
        response = [{'id': a.id, 'nome': a.nome, 'pessoa': a.pessoa.nome}
                    for a in pessoas]
        return response

    def delete(self):
        id = request.json
        atividade = Atividade.query.filter_by(id=id['id']).first()
        print(atividade)
        atividade.delete()
        return {'msg': 'deletado'}


api.add_resource(Dado, '/dev/<string:nome>')
api.add_resource(ListaDados, '/dev')
api.add_resource(Atv, '/atv')

if __name__ == '__main__':
    app.run(debug=True)
