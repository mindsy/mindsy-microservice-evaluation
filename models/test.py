from db import db
import enum


class TypeEnum(enum.Enum):
    verbal = "verbal"
    executivo = "executivo"


class TestModel(db.Model):
    __tablename__ = 'TEST'

    id_test = db.Column('id_test', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100), nullable=False)
    description = db.Column('description', db.String(255))
    maximum_score = db.Column('maximum_score', db.Decimal(4))
    type = db.Column('type', db.Enum(TypeEnum), nullable=False)

    evaluation_tests = db.relationship('EvaluationTestModel', backref='TEST', lazy='dynamic',
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
    #

    def json(self):
        return {
                    'id_test': self.id_test,
                    'name': self.name,
                    'description': self.description,
                    'maximum_score': self.maximum_score,
                    'type': self.type.value
                }

    # @classmethod
    # def find_by_id(cls, id):
    #     return cls.query.filter_by(id_patient=id).first()
    #
    # @classmethod
    # def find_by_registry_number_pat(cls, registry_number_pat):
    #     return cls.query.filter_by(registry_number_pat=registry_number_pat).first()
    #

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
