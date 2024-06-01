from flask_seeder import Seeder
from sqlalchemy import select

from app.model import engine, Country, City, CityTollFeeRate
from app.config import COUNTRY_DATA, CITY_DATA,  CITY_TOLL_FEE_RATE_DATA

def seed_data_to_db(seeder_cls, db_model, data, comment):
     try:	
        data_to_be_added = db_model(**data)
        print(f"Adding {comment}:{ %s}" % datdata_to_be_addeda)
        seeder_cls.db.session.add(data_to_be_added)

    except Exception as e:
        seeder_cls.db.rollback()
        raise e
    else:
        seeder_cls.db.session.commit()

class CountrySeeder(Seeder):
    def __init__(self):
        super().__init__()
        self.priority = 1

    def run(self):
        seed_data_to_db(self, Country, COUNTRY_DATA, "country")
        # try:	
        #     country = Country(**COUNTRY_DATA)
        #     print("Adding country: %s" % country)
        #     self.db.session.add(country)

        # except Exception as e:
        #     self.db.rollback()
        #     raise e
        # else:
        #     self.db.session.commit()

class CitySeeder(Seeder):
    def __init__(self):
        super().__init__()
        self.priority = 2

    def run(self):
        seed_data_to_db(self, City, CITY_DATA, "city")
        # try:	
        #     city = City(**CITY_DATA)
        #     print("Adding city: %s" % city)
        #     self.db.session.add(city)

        # except Exception as e:
        #     self.db.rollback()
        #     raise e
        # else:
        #     self.db.session.commit()

class CityTollFeeRateSeeder(Seeder):
    def __init__(self):
        super().__init__()
        self.priority = 3

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