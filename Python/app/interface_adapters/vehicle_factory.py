from ..use_cases import IVehicleFactory
from .vehicles import Motorbike, Tractor, Emergency, \
    Diplomat, Foreign, Military, Car

class VehicleFactory(IVehicleFactory):

    def get_vehicles(self) -> IVehicleFactory:
        return {
            0: Motorbike(),
            1: Tractor(),
            2: Emergency(),
            3: Diplomat(),
            4: Foreign(),
            5: Military(),
            6: Car(),
        }