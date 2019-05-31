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
    parser.add_argument('classification',
                        type=str,
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

            if data['classification']:
                result.classification_score = data['classification']

        else:
            return {'message': 'Result not found.'}, 404

        result.save_to_db()

        return {'message': 'Result updated.'}, 200
