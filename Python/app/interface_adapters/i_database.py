from abc import ABCMeta, abstractclassmethod

class IDatabase(metaclass=ABCMeta):

    @abstractclassmethod
    def write(self, model, data: dict):
        raise NotImplementedError()