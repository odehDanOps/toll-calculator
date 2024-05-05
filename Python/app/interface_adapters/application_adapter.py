from ..use_cases import  ICalculator

class ApplicationAdapter(ICalculator):
    def __init__(self, service):
        self.service = service

    def get_city_details(self):
        _id = 1
        return self.service.get_city(_id)
    
    def get_city_toll_fee_rates(self):
        _id = 1
        return self.service.get_city_toll_fee_rates(_id)
        
    def get_vehicle_toll_fee(self, vehicle, vehicle_number):
        data = {
            "vehicle": vehicle,
            "vehicle_number": vehicle_number
        }
        return self.service.get_vehicle_toll_fee(data)