from abc import ABCMeta, abstractmethod, abstractproperty

class Service(ABCMeta):
    @abstractmethod
    def do(self):
        pass 

    @abstractmethod
    def get_stats(self):
        pass


    