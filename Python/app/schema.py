from marshmallow import validate

from .model import ma, VehicleTollFee, City, CityTollFeeRate

class VehicleTollFeeSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = (
            "city", "vehicle", 
            "vehicle_number", "date_time",
            "date_time", "fee",
            "created_at", "updated_at"
        )


class CountrySchema(ma.Schema):
    class Meta:
        fields = (
            "name", "currency", 
            "created_at", "updated_at"
        )


class CitySchema(ma.Schema):
    class Meta:
        fields = (
            "name", "country_id", 
            "created_at", "updated_at"
        )


class CityTollFeeRateSchema(ma.Schema):
    class Meta:
        fields = (
            "city_id", "start_time", 
            "end_time", "fee",
            "created_at", "updated_at"
        )


class VehicleTollFeeRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VehicleTollFee

    id = ma.auto_field(dump_only=True)
    city =  ma.auto_field(dump_only=True)
    vehicle =  ma.String(required=True, validate=validate.Length(min=2))
    vehicle_number =  ma.String(required=True)
    date_time = ma.DateTime(required=True)
    fee =  ma.auto_field(dump_only=True)
    last_charged_at =  ma.auto_field(dump_only=True)
    created_at =  ma.auto_field(dump_only=True)
    updated_at =  ma.auto_field(dump_only=True)
    