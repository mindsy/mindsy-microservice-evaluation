from db import db


class EvaluationModel(db.Model):
    __tablename__ = 'EVALUATION'

    id_evaluation = db.Column('id_evaluation', db.Integer, primary_key=True)
    dt_start = db.Column('dt_start', db.DateTime, nullable=False)
    dt_end = db.Column('dt_end', db.DateTime, nullable=False)
    conclusion = db.Column('conclusion', db.Text)
    anamnese = db.Column('anamnese', db.Text)

    test_pat_psycho_hosp_id_pat_psycho_hosp = db.Column('fk_pat_psycho_hosp',
                                                        db.Integer, db.ForeignKey('PAT_PSYCHO_HOSP.id_pat_psycho_hosp'))
    evaluation_tests = db.relationship('EvaluationTestModel', backref='EVALUATION', lazy='dynamic',
                                       cascade='all, delete-orphan')

    # def __init__(self, scholarity, observation, manual_domain, registry_number_pat,
    #              dt_birth, person_pat_id, accountable_patient_registry_acc, status):
    #     self.scholarity = scholarity
    #     self.observation = observation
    #     self.manual_domain = manual_domain
    #     self.registry_number_pat = registry_number_pat
    #     self.dt_birth = dt_birth
    #     self.person_pat_id = person_pat_id
    #     self.accountable_patient_registry_acc = accountable_patient_registry_acc
    #     self.status = status

    def json(self):
        return {
                    'id_evaluation': self.id_evaluation,
                    'dt_start': self.dt_start,
                    'dt_end': self.dt_end,
                    'conclusion': self.conclusion,
                    'anamnese': self.anamnese,
                    'test_pat_psycho_hosp_id_pat_psycho_hosp': self.test_pat_psycho_hosp_id_pat_psycho_hosp,
                    'evaluation_tests': [evaluation_test.json() for evaluation_test in self.evaluation_tests.all()]
                }

    # @classmethod
    # def find_by_id(cls, id):
    #     return cls.query.filter_by(id_patient=id).first()
    #
    # @classmethod
    # def find_by_registry_number_pat(cls, registry_number_pat):
    #     return cls.query.filter_by(registry_number_pat=registry_number_pat).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
