from flask_restful import Resource
from models.evaluation import EvaluationModel


class DeleteEvaluation(Resource):
    @classmethod
    def delete(cls, id_evaluation):
        evaluation = EvaluationModel.find_by_id(id_evaluation)
        if evaluation:
            evaluation.delete_from_db()
            return {'message': 'Evaluation deleted.'}
        return {'message': 'Evaluation not found.'}, 404