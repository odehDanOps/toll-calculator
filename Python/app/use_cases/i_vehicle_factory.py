from abc import ABCMeta, abstractclassmethod

class IVehicleFactory(metaclass=ABCMeta):

    @abstractclassmethod
    def get_vehicles(self):
        """Returns a vehicles name belonging to this factory."""
        raise NotImplementedError()