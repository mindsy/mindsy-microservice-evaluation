from flask_restful import Resource, reqparse
from static.imports import *


class EditResult(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('gross_score',
                        required=False,
                        )
    parser.add_argument('considerate_score',
                        required=False,
                        )

    def put(self, id_result):
        data = EditResult.parser.parse_args()

        result = ResultModel.find_by_id(id_result)

        if result:
            if data['gross_score']:
                result.gross_score = data['gross_score']

            if data['considerate_score']:
                result.considerate_score = data['considerate_score']

                classification = None
                pondered_point = int(data['considerate_score'])

                if pondered_point >= 15:
                    classification = "Superior"

                if 12 <= pondered_point <= 14:
                    classification = "Média Superior"

                if 8 <= pondered_point <= 11:
                    classification = "Média"

                if 5 <= pondered_point <= 7:
                    classification = " Média Inferior"

                if pondered_point <= 4:
                    classification = "Abaixo da Média"

                if classification is None:
                    return {"message": "Something wrong happened"}

                result.classification = classification

        else:
            return {'message': 'Result not found.'}, 404

        result.save_to_db()

        return {'message': 'Result updated.'}, 200
