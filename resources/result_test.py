# -*- coding: utf-8 -*-
from flask_restful import Resource

from static.imports import *
from db import db


class ResultTest(Resource):
    def get(self, id_evaluation):

        if TestModel.find_by_id(id_evaluation):

            tests = (db.session.query(ResultModel)
                     .filter(EvaluationTestModel.test_pat_psycho_hosp_id_evaluation == id_evaluation)
                     .filter(EvaluationTestModel.test_pat_psycho_hosp_id_test == TestModel.id_test)
                     .filter(EvaluationTestModel.id_evaluation_test
                             == ResultModel.evaluation_test_result_id_evaluation_test).all())

            output = []
            for test in tests:

                result_info = test.json()
                result_info.update({'tests': test.EVALUATION_TEST.TEST.json()})
                output.append(result_info)
            return {"results": output}, 200

        else:
            return {"message": "We could not locate this id_evaluation"}, 400
