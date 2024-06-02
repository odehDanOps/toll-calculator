from ..use_cases import  ICalculator

class ApplicationAdapter(ICalculator):
    def __init__(self, service):
        self.service = service

    def get_city_country_details(self):
        country_id = 1 # Manually doing this for now. 
        return self.service.get_city_country(country_id)
    
    def get_city_details(self):
        city_id = 1 # Manually doing this for now. 
        return self.service.get_city(city_id)
    
    def get_city_toll_fee_rates(self):
        _id = 1
        return self.service.get_city_toll_fee_rates(_id)
        
    def get_vehicle_toll_fee(self, vehicle, vehicle_number):
        data = {
            "vehicle": vehicle,
            "vehicle_number": vehicle_number
        }
        return self.service.get_vehicle_toll_fee(data)