import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.create_evaluation import CreateEvaluation
from resources.result import Result
from resources.show_evaluation import ShowEvaluationID
from resources.delete_evaluation import DeleteEvaluation
from resources.test_information import ShowTestInformation

app = Flask(__name__)
load_dotenv(".env")

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = os.environ.get("APP_SECRET_KEY")
app.config['JWT_SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)
api.add_resource(CreateEvaluation, '/evaluation')
api.add_resource(ShowEvaluationID, '/evaluation/<int:id_evaluation>')
api.add_resource(Result, '/test/<string:name_test>')
api.add_resource(DeleteEvaluation, '/delete-evaluation/<int:id_evaluation>')
api.add_resource(ShowTestInformation, '/test-info/<int:id_test>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')
