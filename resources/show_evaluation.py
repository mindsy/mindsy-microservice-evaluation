#-*- coding: utf-8 -*-
from flask_restful import Resource

from static.imports import *


class ShowEvaluationID(Resource):
    def get(self, id_evaluation):
        evaluation = EvaluationModel.find_by_id(id_evaluation)
        if evaluation:
            evaluation_info = evaluation.json()
            all_evaluations = evaluation.evaluation_tests.all()
            flag = []
            for ev in all_evaluations:
                test_info = ev.TEST.json()
                flag.append(test_info)
                result_info = ev.results.json()
                test_info.update({'results': result_info})

            evaluation_info.update({'tests': flag})

            return evaluation_info

        return {'message': 'Evaluation not found.'}, 404

