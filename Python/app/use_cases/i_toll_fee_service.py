from abc import ABCMeta, abstractmethod


class ITollFeeService(metaclass=ABCMeta):
    
    @abstractmethod
    def set_toll_fee(self)-> None:
        raise NotImplementedError()