import time

from apps.utils.model.service import *
from apps.utils.model.preprocess import *
from apps.utils.model.output import *

class ScrapperService(Service):
    def __init__ (self, algo):
        super().__init__(algo, WebPreprocessor(), JsonOutputter())