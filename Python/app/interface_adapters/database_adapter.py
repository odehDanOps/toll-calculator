from ..use_cases import ITollFeeService

class DatabaseAdapter(ITollFeeService):
    def __init__(self, database):
        self.database = database

    def set_toll_fee(self, model, data: dict):
        return  self.database.write(model, data)