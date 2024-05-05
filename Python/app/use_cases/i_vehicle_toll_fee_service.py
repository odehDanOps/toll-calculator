from abc import ABCMeta, abstractmethod


class IVehicleTollFeeService(metaclass=ABCMeta):
    @abstractmethod
    def get_city(self, model, _id: int)-> None:
        raise NotImplementedError()
    
    @abstractmethod
    def get_city_toll_fee_rates(self, model, column, value)-> None:
        raise NotImplementedError()
    
    @abstractmethod
    def set_vehicle_toll_fee(self, model, data: dict)-> None:
        raise NotImplementedError()