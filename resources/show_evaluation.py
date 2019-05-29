#-*- coding: utf-8 -*-
from flask_restful import Resource

from static.imports import *


class ShowEvaluationID(Resource):
    def get(self, id_evaluation):

        evaluation = EvaluationModel.find_by_id(id_evaluation)
        if evaluation:
            evaluation_info = evaluation.json()

            output = {'Evaluation Information': [evaluation_info]}

            return {'Show Information': output}

        return {'message': 'User not found.'}, 404
