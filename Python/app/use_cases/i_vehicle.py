from abc import ABCMeta, abstractclassmethod

class IVehicle(metaclass=ABCMeta):

    @abstractclassmethod
    def vehicle_type(self):
        """Returns a vehicle type."""
        raise NotImplementedError()