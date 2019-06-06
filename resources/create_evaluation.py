# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse
from datetime import datetime
from static.imports import *
from db import db


class CreateEvaluation(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('conclusion',
                        type=str,
                        required=False,
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
                        required=False,
                        type=lambda d: datetime.strptime(d, '%d-%m-%Y')
                        )
    parser.add_argument('crp',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('id_patient',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = CreateEvaluation.parser.parse_args()

        if PatientModel.find_by_id(data['id_patient']) and PsychologistModel.find_by_crp(data['crp']):

            pat_psycho_hosp = (db.session.query(PatPsychoHospModel)
                               .filter(PatientModel.id_patient == data['id_patient'])
                               .filter(HospitalModel.registry_number == "4002")
                               .filter(PsychologistModel.crp == data['crp'])
                               .filter(PatientModel.id_patient == PatPsychoHospModel.patient_hosp_psy_id_patient)
                               .filter(PsychologistHospitalModel.id_psycho_hosp
                                       == PatPsychoHospModel.pat_psycho_hosp_id_psycho_hosp).all())

            new_evaluation = EvaluationModel(data['dt_start'], data['dt_end'], data['conclusion'], data['anamnese'],
                                             pat_psycho_hosp[0].id_pat_psycho_hosp
                                             )
            new_evaluation.save_to_db()
            return {"message": "Evaluation created successfully."}, 201

        return {"message": "We cannot create evaluation"}


