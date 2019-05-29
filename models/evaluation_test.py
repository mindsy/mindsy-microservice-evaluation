from db import db


class EvaluationTestModel(db.Model):
    __tablename__ = 'EVALUATION_TEST'

    id_evaluation_test = db.Column('id_evaluation_test', db.Integer, primary_key=True)

    test_pat_psycho_hosp_id_evaluation = db.Column('fk_evaluation',
                                                   db.Integer, db.ForeignKey('EVALUATION.id_evaluation'))
    test_pat_psycho_hosp_id_test = db.Column('fk_test',
                                             db.Integer, db.ForeignKey('TEST.id_test'))

    psychologists = db.relationship('ResultModel', backref='EVALUATION_TEST', uselist=False,        #result???
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
                    'id_evaluation_test': self.id_evaluation_test,
                    'test_pat_psycho_hosp_id_evaluation': self.test_pat_psycho_hosp_id_evaluation,
                    'test_pat_psycho_hosp_id_test': self.test_pat_psycho_hosp_id_test,
                    'result:': self.psychologists                   # Nao seria result ao inves de psychologists???
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
