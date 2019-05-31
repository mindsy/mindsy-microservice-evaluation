#-*- coding: utf-8 -*-
from flask_restful import Resource

from static.imports import *


class ShowEvaluationID(Resource):
    def get(self, id_evaluation):

        evaluation = EvaluationModel.find_by_id(id_evaluation)
        if evaluation:
            evaluation_info = evaluation.json()

            return {'evaluation': evaluation_info}

        return {'message': 'Evaluation not found.'}, 404
