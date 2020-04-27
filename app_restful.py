from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import ListaHabilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0, 'nome': 'isabela', 'habilidades': ['Python', 'Flask']},
    {'id': 1, 'nome': 'oliveira', 'habilidades': ['Python', 'Django']}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        status = {'status': 'sucesso', 'mensagem': 'registro excluido'}
        return status


class ListaDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return {'status': 'sucesso', 'mensagem': 'registro adicionado'}

    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(ListaHabilidades, '/dev/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
