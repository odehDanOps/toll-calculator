from .interface_adapters import ApplicationAdapter, SQLAdapter, DatabaseAdapter, VehicleFactory
from .use_cases import TollFee
from .database import engine
from .models.toll_fee import Base

def run_app():
    Base.metadata.create_all(engine)
    sql_adapter = SQLAdapter(engine)
    database_adapter = DatabaseAdapter(sql_adapter)

    vehicle_factory = VehicleFactory()
    vehicles = vehicle_factory.get_vehicles()
    for vehicle_uuid, vehicle in vehicles.items():
        print(f"{vehicle}: {vehicle_uuid}")

    # Get user input for the index
    while True:
        try:
            vehicle_type_number = int(input("Enter vehicle type (0,1,2...): "))
            if 0 <= vehicle_type_number <= 6:
                break
            else:
                print("Invalid vehicle type. Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter vehicle type number.")
    
    vehicle_number = input("Enter vehicle license number: ")

    if vehicle_type_number in vehicles:
        vehicle_class = vehicles[vehicle_type_number]

        vehicle = vehicle_class.vehicle_type()
        toll_fee_service = TollFee(database_adapter)
        app = ApplicationAdapter(toll_fee_service)
        app.get_toll_fee(vehicle, vehicle_number)
    else:
        print("The entered vehicle type does not exist in the availabe vehicles.")