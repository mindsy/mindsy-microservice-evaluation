from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from db import db
from flask_cors import CORS

from static.resource_imports import *
from flask_cors import CORS


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://db3mp2dauwixvkcg:t3hkuoethj9xvd1l@u0zbt18wwjva9e0v.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/w63zlckiy2z278iv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
CORS(app)
db.init_app(app)

api.add_resource(CreateEvaluation, '/evaluation')
api.add_resource(EditEvaluation, '/evaluation/<int:id_evaluation>')
api.add_resource(ShowEvaluationID, '/evaluation/<int:id_evaluation>')
api.add_resource(DeleteEvaluation, '/delete-evaluation/<int:id_evaluation>')
api.add_resource(PsychologistEvaluationPatient, '/psychologist-evaluation/<string:crp>/<int:id_patient>')

api.add_resource(Result, '/result/<int:id_test>')
api.add_resource(EditResult, '/result/<int:id_result>')
api.add_resource(ResultTest, '/result/<int:id_evaluation>')
api.add_resource(WiscList, '/wisc-list')
api.add_resource(DeleteResult, '/delete-result/<int:id_result>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
