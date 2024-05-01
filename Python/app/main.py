from .interface_adapters import ApplicationAdapter, SQLAdapter, DatabaseAdapter
from .use_cases import TollFee
from .database import engine
from .models.toll_fee import Base

def run_app():
    Base.metadata.create_all(engine)
    sql_adapter = SQLAdapter(engine)
    database_adapter = DatabaseAdapter(sql_adapter)

    vehicle= input("Enter vehicle type: ")
    vehicle_number = input("Enter vehicle number: ")

    toll_fee_service = TollFee(database_adapter)
    app = ApplicationAdapter(toll_fee_service)
    app.get_toll_fee(vehicle, vehicle_number)