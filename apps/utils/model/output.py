from abc import ABCMeta, abstractmethod
from flask import jsonify
from typing import Dict, Any
from apps.utils.model.error import OutputException
import logging 

LOG = logging.getLogger(__name__)

class Outputter(object):
    @abstractmethod
    def output(self, data):
        pass

class JsonOutputter(Outputter):
    def output(self, data) -> Dict[str, Any]:
        LOG.info("Start Outputing Result")
        return jsonify(**data)