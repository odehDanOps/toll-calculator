from flask import Flask, Blueprint, redirect, url_for, jsonify, abort
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from apifairy import body, response, other_responses

from .interface_adapters import ApplicationAdapter, SQLAdapter, DatabaseAdapter
from .use_cases import VehicleTollFee
from .model import engine as db, ma
from apifairy import APIFairy

migrate = Migrate(db=db)
apifairy = APIFairy()
bp = Blueprint('fees', __name__)

def routes(application_adapter):
    from .schema import CountrySchema, CitySchema, VehicleTollFeeSchema, \
        VehicleTollFeeRequestSchema, CityTollFeeRateSchema
    country_schema = CountrySchema()
    city_schema = CitySchema()
    vehicle_toll_fees_request_schema = VehicleTollFeeRequestSchema()
    vehicle_toll_fee_schema = VehicleTollFeeSchema()
    city_toll_fee_rate_schema = CityTollFeeRateSchema(many=True)

    @bp.route('/')
    def index():  # pragma: no cover
        return redirect(url_for('apifairy.docs'))
    
    
    @bp.route('/city/country', methods=['GET'])
    @response(country_schema)
    @other_responses({404: 'Country not found'})
    def get_city_country():
        response = application_adapter.get_city_country_details()
        if response:
            return response
        
    
    @bp.route('/city/detail', methods=['GET'])
    @response(city_schema)
    @other_responses({404: 'City not found'})
    def get_city():
        response = application_adapter.get_city_details()
        if response:
            return response
    

    @bp.route('/city/rates', methods=['GET'])
    @response(city_toll_fee_rate_schema)
    @other_responses({404: 'City rates not found'})
    def get_city_rates():
        responses = application_adapter.get_city_toll_fee_rates()
        if responses:
            return responses
    

    @bp.route('/city/vehicle/fees', methods=['POST'])
    @body(vehicle_toll_fees_request_schema)
    @response(vehicle_toll_fees_request_schema, 201)
    @other_responses({403: 'Forbidden'})
    def calculate_vehicle_toll_fee_rate(vehicle, vehicle_number):
        responses = application_adapter.get_vehicle_toll_fee(vehicle, vehicle_number)
        if responses:
            return jsonify(responses)
        abort(403)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    apifairy.init_app(app)

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