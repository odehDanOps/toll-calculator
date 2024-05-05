from flask_seeder import Seeder
from sqlalchemy import select

from app.model import engine, City, CityTollFeeRate
from app.config import CITY_DATA,  CITY_TOLL_FEE_RATE_DATA

class CitySeeder(Seeder):
    def __init__(self):
        super().__init__()
        self.priority = 1

    def run(self):
        try:	
            city = City(**CITY_DATA)
            print("Adding city: %s" % city)
            self.db.session.add(city)

        except Exception as e:
            self.db.rollback()
            raise e
        else:
            self.db.session.commit()

class CityTollFeeRateSeeder(Seeder):
    def __init__(self):
        super().__init__()
        self.priority = 2

    def run(self):
        city_id = self.db.session.scalar(select(City.id).where(
                    City.name == CITY_DATA["name"]))
        rates = []
        try:
            for rate in CITY_TOLL_FEE_RATE_DATA:
                rate["city_id"] = city_id
                print("Adding rate: %s" % rate)
                rates.append(CityTollFeeRate(**rate))
            self.db.session.add_all(rates)

        except Exception as e:
            self.db.rollback()
            raise e
        else:
            self.db.session.commit()