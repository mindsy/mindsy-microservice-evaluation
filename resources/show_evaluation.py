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
                flag2 = []
                result_info = ev.results.json()
                flag2.append(result_info)

                test_info.update({'results': flag2})

            evaluation_info.update({'tests': flag})

            return {'evaluation': evaluation_info}

        return {'message': 'Evaluation not found.'}, 404

