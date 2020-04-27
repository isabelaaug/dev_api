from flask import Flask, request
from flask_restful import Resource, Api
import json

lista_habilidades = ['Python', 'Java', 'JavaScript', 'PHP', 'Django', 'Flask']


class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades
