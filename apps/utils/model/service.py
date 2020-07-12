from abc import abstractmethod, abstractproperty
from typing import Dict, Any

class Service(object):
    @abstractproperty
    def data(self):
        pass 

    @abstractmethod
    def get_stats(self) -> Dict[str, Any]:
        pass 

