# -*- coding: utf-8 -*-
from flask_restful import Resource

from static.imports import *
from db import db


class PsychologistEvaluationPatient(Resource):
    def get(self, crp, id_patient):

        if PsychologistModel.find_by_crp(crp) and PatientModel.find_by_id(id_patient):

            evaluations = (db.session.query(EvaluationModel)
                           .filter(HospitalModel.registry_number == '4002')
                           .filter(PsychologistModel.crp == crp)
                           .filter(PatientModel.id_patient == id_patient)
                           .filter(PsychologistHospitalModel.id_psycho_hosp ==
                                   PatPsychoHospModel.pat_psycho_hosp_id_psycho_hosp)
                           .filter(PatientModel.id_patient == PatPsychoHospModel.patient_hosp_psy_id_patient)
                           .filter(PatPsychoHospModel.id_pat_psycho_hosp ==
                                   EvaluationModel.test_pat_psycho_hosp_id_pat_psycho_hosp).all())

            output = []
            for evaluation in evaluations:

                evaluation_info = evaluation.json()
                output.append(evaluation_info)
            return {"evaluations": output}, 200

        else:
            return {"message": "We could not locate this crp or we could not locate this id_patient"}, 400
