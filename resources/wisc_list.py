# -*- coding: utf-8 -*-
from flask_restful import Resource

from static.imports import *
from db import db


class WiscList(Resource):
    def get(self):

        tests = db.session.query(TestModel).all()
        if tests:
            output = []
            for test in tests:

                test_info = test.json()
                output.append(test_info)
            return {"tests": output}, 200

        return {"message": "Something Wrong happened"}, 500
