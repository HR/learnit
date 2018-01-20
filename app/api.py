#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
api.py -
"""

from flask import request
from flask_restful import Resource, Api, fields, reqparse

from app import app
from db import session
from models import Data, Questions

api = Api(app)

data_fields = {
    'data': fields.String,
}

parser = reqparse.RequestParser()
parser.add_argument('data', type=str)

test = {}


class KnowledgeData(Resource):

    def get(self, id):
        data = session.query(Data).filter(Data.id == id).first()
        return data

    def post(self):
        parsed_args = parser.parse_args()
        data = Data(data=parsed_args['data'])

        # session.add(data)
        # session.commit()
        return data.data

    def delete(self):
        pass


class KnowledgeQuestions(Resource):

    def get(self, id):
        questions = session.query(Questions).filter(Questions.id == id).first()
        return questions

    def post(self):
        parsed_args = parser.parse_args()
        questions = Questions(questions=parsed_args['data'])
        db.session.add(data)
        db.session.commit()
        return jsonify({'questions': questions}), 201

    def delete(self):
        pass

api.add_resource(KnowledgeData, '/source/<int:id>')
api.add_resource(KnowledgeQuestions, '/questions/<int:id>')
