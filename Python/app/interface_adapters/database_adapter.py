from ..use_cases import IVehicleTollFeeService

class DatabaseAdapter(IVehicleTollFeeService):
    def __init__(self, database):
        self.database = database
        self.city = None
        self.city_toll_fee_rates = None

    def bootstrap_city(self, model, _id: int):
        self.city = self.database.get(model, _id)
        return  self.city
    
    def bootstrap_city_toll_fee_rate(self, model, _id: int):
        self.city_toll_fee_rates = self.database.get_all_city_rates(model, _id)
        return  self.city_toll_fee_rates

    def get_city(self, model, _id: int):
        return  self.city if self.city else self.bootstrap_city(model, _id)
    
    def get_city_toll_fee_rates(self, model, _id):
        return  self.city_toll_fee_rates if self.city_toll_fee_rates else self.bootstrap_city_toll_fee_rate(model, _id)
    
    def set_vehicle_toll_fee(self, model, data: dict):
        return  self.database.write(model, data)