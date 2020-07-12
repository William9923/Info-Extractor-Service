from abc import abstractmethod, abstractproperty

class Service(object):
    @abstractmethod
    def preprocess(self, request):
        pass

    @abstractproperty
    def data(self):
        pass 

    @abstractmethod
    def get_stats(self):
        pass 

