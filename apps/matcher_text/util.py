from apps.utils.model.algorithm import *

from apps.matcher_text.service import *
from apps.matcher_text.output import *
from apps.matcher_text.preprocess import *

class ServiceFactory(object):
    def __init__(self, inputs):
        self.algo = inputs.get('algo')
        self.keyword = inputs.get('keyword')
        self.content = inputs.get('content')

    def create_service(self):
        return TextService(self.find_algo(), TextPreprocessor(), TextOutputter())

    def find_algo(self):
        if self.algo == 'kmp' : 
            return KMPAlgorithm()
        elif self.algo == 'bm' : 
            return BMAlgorithm()
        return RegexAlgorithm()

    def zip_data(self):
        return {
            'keyword' : self.keyword,
            'content' : self.content
        }
