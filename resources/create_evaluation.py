# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse

from datetime import datetime

from static.imports import *


class CreateEvaluation(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('conclusion',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('anamnese',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('dt_start',
                        type=lambda d: datetime.strptime(d, '%d-%m-%Y')
                        )
    parser.add_argument('dt_end',
                        type=lambda d: datetime.strptime(d, '%d-%m-%Y')
                        )
    parser.add_argument('test_pat_psycho_hosp_id_pat_psycho_hosp',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = CreateEvaluation.parser.parse_args()

        new_evaluation = EvaluationModel(data['dt_start'], data['dt_end'], data['conclusion'], data['anamnese'],
                                         data['test_pat_psycho_hosp_id_pat_psycho_hosp'])
        new_evaluation.save_to_db()
        return {"message": "Evaluation created successfully.", "id_evaluation": new_evaluation.id_evaluation}, 201


