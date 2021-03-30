from flask_restful import Resource
hablidades = ['python', 'java']


class Habilidade(Resource):
    def get(self):
        return hablidades
