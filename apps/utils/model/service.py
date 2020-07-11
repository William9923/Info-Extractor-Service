from abc import ABCMeta, abstractmethod

class Service(ABCMeta):
    @abstractmethod
    def Do(self):
        pass 
