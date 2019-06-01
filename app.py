import os
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from static.resource_imports import *


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
api.add_resource(EditEvaluation, '/evaluation/<int:id_evaluation>')
api.add_resource(ShowEvaluationID, '/evaluation/<int:id_evaluation>')
api.add_resource(DeleteEvaluation, '/delete-evaluation/<int:id_evaluation>')

api.add_resource(Result, '/result/<int:id_test>')
api.add_resource(PsychologistEvaluationPatient, '/psychologist-evaluation/<string:crp>/<int:id_patient>')
api.add_resource(EditResult, '/result/<int:id_result>')
api.add_resource(ResultTest, '/result/<int:id_evaluation>')
api.add_resource(WiscList, '/wisc-list')
api.add_resource(DeleteResult, '/delete-result/<int:id_result>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')
