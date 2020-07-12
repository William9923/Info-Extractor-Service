from abc import ABCMeta, abstractmethod
from flask import jsonify


class Outputter(object):
    @abstractmethod
    def output(self, data):
        pass

class JsonOutputter(Outputter):
    def output(self, data):
        return jsonify(**data)