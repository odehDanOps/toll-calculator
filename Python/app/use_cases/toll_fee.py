from .i_toll_fee_service import ITollFeeService
from ..models.toll_fee import TollFee as TollFeeModel

class TollFee:
    def __init__(self, database_service: ITollFeeService):
        self.database_service = database_service
        self.model = TollFeeModel

    def get_toll_fee(self, data: dict):
        return self.database_service.set_toll_fee(self.model, data)