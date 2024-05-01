from ..use_cases import  ICalculator

class ApplicationAdapter(ICalculator):
    def __init__(self, service):
        self.service = service

    
    def get_toll_fee(self, vehicle, vehicle_number):
        data = {
            "vehicle": vehicle,
            "vehicle_number": vehicle_number
        }
        return self.service.get_toll_fee(data)