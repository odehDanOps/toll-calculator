from .i_vehicle_toll_fee_service import IVehicleTollFeeService
from ..model import City, CityTollFeeRate, VehicleTollFee as VehicleTollFeeModel

class VehicleTollFee:
    def __init__(self, database_service: IVehicleTollFeeService):
        self.database_service = database_service
        self.city_model = City
        self.city_toll_fee_rate_model = CityTollFeeRate
        self.vehicle_toll_fee_model = VehicleTollFeeModel

    def get_city(self, _id: int):
        return self.database_service.get_city(self.city_model, _id)
    
    def get_city_toll_fee_rates(self, _id: int):
        return self.database_service.get_city_toll_fee_rates(self.city_toll_fee_rate_model, _id)
    
    def get_vehicle_toll_fee(self, data: dict):
        city_id = data.get("id")
        if city_id:
            city_toll_fee_rates = self.get_city_toll_fee_rates(data.get("id"))
            city_toll_fee_rates_refined_array = []
            for rate in city_toll_fee_rates:
                array = {
                    "end_time": rate.end_time,
                    "fee": rate.fee,
                    "start_time": rate.start_time
                }
                city_toll_fee_rates_refined_array.append(array)
            return city_toll_fee_rates_refined_array
            # return self.database_service.set_vehicle_toll_fee(self.vehicle_toll_fee_model, data)