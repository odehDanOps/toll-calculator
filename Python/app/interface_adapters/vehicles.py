from ..use_cases import IVehicle

class Motorbike(IVehicle):
    def __init__(self):
        self.vehicle = "Motorbike"
        
    def __str__(self):
        return self.vehicle

    def vehicle_type(self):
        return self.vehicle
    
class Tractor(IVehicle):
    def __init__(self):
        self.vehicle = "Tractor"

    def __str__(self):
        return self.vehicle

    def vehicle_type(self):
        return self.vehicle
    

class Emergency(IVehicle):
    def __init__(self):
        self.vehicle = "Emergency"

    def __str__(self):
        return self.vehicle

    def vehicle_type(self):
        return self.vehicle
    

class Diplomat(IVehicle):
    def __init__(self):
        self.vehicle = "Diplomat"

    def __str__(self):
        return self.vehicle

    def vehicle_type(self):
        return self.vehicle
    

class Foreign(IVehicle):
    def __init__(self):
        self.vehicle = "Foreign"

    def __str__(self):
        return self.vehicle

    def vehicle_type(self):
        return self.vehicle
    

class Military(IVehicle):
    def __init__(self):
        self.vehicle = "Military"

    def __str__(self):
        return self.vehicle

    def vehicle_type(self):
        return self.vehicle
    

class Car(IVehicle):
    def __init__(self):
        self.vehicle = "Car"

    def __str__(self):
        return self.vehicle

    def vehicle_type(self):
        return self.vehicle