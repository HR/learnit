#!/usr/bn/env python
# -*- coding: utf-8 -*-
"""
api.py -
"""

from flask import request, jsonify
from flask_restful import Resource, Api, fields, reqparse

from app import app
from db import session
from models import Data, Questions
from serve import model_api

# api = Api(app)

data_fields = {
    'data': fields.String,
}

parser = reqparse.RequestParser()
parser.add_argument('data', type=str)

test = {}


@app.route('/learn', methods=['POST'])
def learn():
    input_data = request.form
    output_data = model_api(
        input_data['source'], input_data['question[text]'], input_data['answer'])
    response = {'correct': 1 if output_data else 0}
    return jsonify(response)


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


# api.add_resource(KnowledgeData, '/source/<int:id>')
# api.add_resource(KnowledgeQuestions, '/questions/<int:id>')
