import time

from apps.utils.model.service import Service
from apps.utils.model.preprocess import URLPreprocessor
from apps.utils.model.output import JsonOutputter

class ScrapperService(Service):
    def __init__ (self, algo):
        super().__init__(algo, URLPreprocessor(), JsonOutputter())