from abc import ABCMeta, abstractmethod

class Outputter(metaclass=ABCMeta):
    @abstractmethod
    def output(self, data):
        pass