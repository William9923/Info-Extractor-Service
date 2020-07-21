import time

from apps.utils.model.service import *
from apps.utils.model.preprocess import *
from apps.utils.model.output import *

class TextService(Service):
    def __init__ (self, algo):
        self.super.__init__(algo, TextPreprocessor(), JsonOutputter())
