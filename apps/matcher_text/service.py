import time

from apps.utils.model.service import Service
from apps.utils.model.preprocess import TextPreprocessor
from apps.utils.model.output import JsonOutputter

class TextService(Service):
    def __init__ (self, algo):
        super().__init__(algo, TextPreprocessor(), JsonOutputter())
