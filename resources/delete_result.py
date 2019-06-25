from flask_restful import Resource
from models.result import ResultModel


class DeleteResult(Resource):
    @classmethod
    def delete(cls, id_result):
        result = ResultModel.find_by_id(id_result)
        if result:
            result.EVALUATION_TEST.delete_from_db()
            result.delete_from_db()
            return {'message': 'Result deleted.'}
        return {'message': 'Result not found.'}, 404