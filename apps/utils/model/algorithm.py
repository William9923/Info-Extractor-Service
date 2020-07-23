from abc import ABCMeta, abstractmethod, abstractproperty
from typing import List

from apps.utils.kmp import knuth_morris_prath
from apps.utils.bm import boyer_moore
from apps.utils.regex import regex_function

class BaseAlgorithm(metaclass=ABCMeta):
    @abstractmethod
    def find(self) -> List[int]:
        pass 

    @abstractproperty
    def pattern(self) -> str:
        pass 

    @abstractproperty
    def text(self) -> str:
        pass 

class KMPAlgorithm(BaseAlgorithm):

    def find(self) -> List[int]:
        return knuth_morris_prath(self._pattern, self._text)
    
    @property
    def pattern(self) -> str:
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        self._pattern = value

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def __repr__(self):
        return "KMP Algorithm"


class BMAlgorithm(BaseAlgorithm):

    def find(self) -> List[int]:
        return boyer_moore(self._pattern, self._text)

    @property
    def pattern(self) -> str:
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        self._pattern = value

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def __repr__(self):
        return "BM Algorithm"


class RegexAlgorithm(BaseAlgorithm):

    def find(self) -> List[int]:
        return regex_function(self._pattern, self._text)

    @property
    def pattern(self) -> str:
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        self._pattern = value

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def __repr__(self):
        return "Regex Algorithm"

class AlgorithmFactory(object):
    def getAlgo(self, format):
        if format == "kmp":
            return KMPAlgorithm()
        elif format == "bm":
            return BMAlgorithm()
        elif format == "regex":
            return RegexAlgorithm()
        else :
            raise ValueError(format)






