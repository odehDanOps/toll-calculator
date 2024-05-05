from ..use_cases import IVehicleTollFeeService

class DatabaseAdapter(IVehicleTollFeeService):
    def __init__(self, database):
        self.database = database

    def get_city(self, model, id: int):
        return  self.database.get(model, id)
    
    def get_city_toll_fee_rates(self, model, _id):
        return  self.database.get_all_city_rates(model, _id)
    
    def set_vehicle_toll_fee(self, model, data: dict):
        return  self.database.write(model, data)