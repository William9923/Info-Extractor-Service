from apps.utils.model.output import *
from flask import jsonify

class TextOutputter():
    def output(self, data):
        return jsonify(**data)