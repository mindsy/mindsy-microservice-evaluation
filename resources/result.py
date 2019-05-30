# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse
from static.imports import *


class Result(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('gross_score',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('considerate_score',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('id_evaluation',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self, name_test):
        test = TestModel.find_by_name(name_test)

        if test:
            data = Result.parser.parse_args()
            new_evaluation_test = EvaluationTestModel(data['id_evaluation'],
                                                      test.id_test)
            new_evaluation_test.save_to_db()

            classification = None
            pondered_point = int(data['considerate_score'])
            if pondered_point > 15:
                classification = "Classificação Superior"

            if 12 <= pondered_point <= 14:
                classification = "Classificação Média Superior"

            if 8 <= pondered_point <= 11:
                classification = " Classificação Média"

            if 5 <= pondered_point <= 7:
                classification = " Classificação Média Inferior"

            if pondered_point <= 4:
                classification = " Classificação Abaixo da Média (prejuízo)"

            if classification is None:
                return {"message": "Something wrong happened"}

            new_result = ResultModel(data['gross_score'], data['considerate_score'],
                                     classification, test.id_test)
            new_result.save_to_db()

            return {"message": "Result created successfully."}, 201

        return {'message': 'Test not found.'}, 404
