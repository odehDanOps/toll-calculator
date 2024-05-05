from abc import ABCMeta, abstractclassmethod

class IDatabase(metaclass=ABCMeta):

    @abstractclassmethod
    def get(self, model, _id: int):
        raise NotImplementedError()
    
    @abstractclassmethod
    def get_all_city_rates(self, model, id):
        raise NotImplementedError()
    
    @abstractclassmethod
    def write(self, model, data: dict):
        raise NotImplementedError()