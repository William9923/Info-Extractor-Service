from abc import ABCMeta, abstractmethod

from apps.utils.kmp import knuth_morris_prath
from apps.utils.bm import boyer_moore
from apps.utils.regex import regex_function

class BaseAlgorithm(metaclass=ABCMeta):
    @abstractmethod
    def find(self):
        pass 

class KMPAlgorithm(BaseAlgorithm):
    def __init__(self, pattern, text):
        self.pattern = pattern 
        self.text = text 

    def find(self):
        return knuth_morris_prath(self.pattern, self.text)


class BMAlgorithm(BaseAlgorithm):
    def __init__(self, pattern, text):
        self.pattern = pattern 
        self.text = text 

    def find(self):
        return boyer_moore(self.pattern, self.text)

class RegexAlgorithm(BaseAlgorithm):
    def __init__(self, pattern, text):
        self.pattern = pattern 
        self.text = text 

    def find(self):
        return regex_function(self.pattern, self.text)



