from flask_restful import Resource, reqparse
from static.imports import *
from datetime import datetime


class EditEvaluation(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('dt_start',
                        type=lambda d: datetime.strptime(d, '%d-%m-%Y'),
                        required=False,
                        help="Invalid date format."
                        )
    parser.add_argument('dt_end',
                        type=lambda d: datetime.strptime(d, '%d-%m-%Y'),
                        required=False,
                        help="Invalid date format."
                        )
    parser.add_argument('conclusion',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('anamnese',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )

    def put(self, id_evaluation):
        data = EditEvaluation.parser.parse_args()

        evaluation = EvaluationModel.find_by_id(id_evaluation)

        if evaluation:
            if data['dt_start']:
                evaluation.dt_start = data['dt_start']

            if data['dt_end']:
                evaluation.dt_end = data['dt_end']

            if data['conclusion']:
                evaluation.conclusion = data['conclusion']

            if data['anamnese']:
                evaluation.anamnese = data['anamnese']

        else:
            return {'message': 'Evaluation not found.'}, 404

        evaluation.save_to_db()

        return {'message': 'Evaluation updated.'}, 200