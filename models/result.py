from db import db


class ResultModel(db.Model):
    __tablename__ = 'RESULT'

    id_result = db.Column('id_result', db.Integer, primary_key=True)
    gross_score = db.Column('gross_score', db.Decimal, nullable=False)
    considerate_score = db.Column('considerate_score', db.Decimal, nullable=False)
    classification = db.Column('classification', db.String(20), nullable=False)

    evaluation_test_result_id_evaluation_test = db.Column('fk_evaluation_test',
                                                          db.Integer, db.ForeignKey('EVALUATION_TEST.id_person'),
                                                          unique=True, nullable=False)

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
    #
    # def json(self):
    #     return {
    #         'id_patient': self.id_patient, 'scholarity': self.scholarity, 'observation': self.observation,
    #         'manual_domain': self.manual_domain.value, 'registry number': self.registry_number_pat,
    #         'date of birth': self.dt_birth.strftime("%d-%m-%Y"), 'status': self.status.value
    #     }
    #
    # @classmethod
    # def find_by_id(cls, id):
    #     return cls.query.filter_by(id_patient=id).first()
    #
    # @classmethod
    # def find_by_registry_number_pat(cls, registry_number_pat):
    #     return cls.query.filter_by(registry_number_pat=registry_number_pat).first()
    #
    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()
    #
    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()