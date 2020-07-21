from abc import ABCMeta, abstractmethod
from flask import jsonify
from typing import Dict, Any

class Outputter(object):
    @abstractmethod
    def output(self, data):
        pass

class JsonOutputter(Outputter):
    def output(self, data) -> Dict[str, Any]:
        return jsonify(**data)