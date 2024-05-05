from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask import jsonify

from .interface_adapters import ApplicationAdapter, SQLAdapter, DatabaseAdapter
from .use_cases import VehicleTollFee
# from .database import engine
from .model import engine as db
from.config import CITY_VEHICLES as city_vehicles

migrate = Migrate(db=db)
bp = Blueprint('fees', __name__)

def routes(application_adapter):
    @bp.route('/city/detail', methods=['GET'])
    def get_city():
        response = application_adapter.get_city_details()
        if response:
            return jsonify(response.to_dict())
        return {
                "message": "Company not found"
            }, 200
    
    @bp.route('/city/rates', methods=['GET'])
    def get_city_rates():
        responses = application_adapter.get_city_toll_fee_rates()
        if responses:
            items = []
            for row in responses:
                items.append(row.to_dict())
            return jsonify(items)
        return {
                "message": "Company rates not found"
            }, 200

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    sql_adapter = SQLAdapter(db)
    database_adapter = DatabaseAdapter(sql_adapter)

    vehicle_toll_fee_service = VehicleTollFee(database_adapter)
    application_adapter = ApplicationAdapter(vehicle_toll_fee_service)
    routes(application_adapter)

    app.register_blueprint(bp, url_prefix='/fees')


    return app
from .model import City, CityTollFeeRate, VehicleTollFee as VehicleTollFeeModel
    
    # for vehicle_uuid, vehicle in city_vehicles.items():
    #     print(f"{vehicle}: {vehicle_uuid}")

    # # Get user input for the index
    # while True:
    #     try:
    #         vehicle_type_number = int(input("Enter vehicle type (0,1,2...): "))
    #         if 0 <= vehicle_type_number <= 6:
    #             break
    #         else:
    #             print("Invalid vehicle type. Please enter a number between 0 and 6.")
    #     except ValueError:
    #         print("Invalid input. Please enter vehicle type number.")
    
    # vehicle_number = input("Enter vehicle license number: ")

    # if vehicle_type_number in city_vehicles:
    #     vehicle_class = city_vehicles[vehicle_type_number]

    #     vehicle = vehicle_class.vehicle_type()
    #     vehicle_toll_fee_service = VehicleTollFee(database_adapter)
    #     app = ApplicationAdapter(vehicle_toll_fee_service)
    #     app.get_vehicle_toll_fee(vehicle, vehicle_number)
    # else:
    #     print("The entered vehicle type does not exist in the availabe vehicles.")