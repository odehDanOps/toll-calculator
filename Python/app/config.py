import pytz
from datetime import time

from .interface_adapters.vehicles import Motorbike, Tractor, Emergency, \
    Diplomat, Foreign, Military, Car, Buss

COUNTRY_TIME_ZONE = pytz.timezone('Europe/Stockholm')
CURRENCY = "SEK"
# Vehicles in Gothenburg
CITY_VEHICLES = {
    0: Motorbike(),
    1: Tractor(),
    2: Emergency(),
    3: Diplomat(),
    4: Foreign(),
    5: Military(),
    6: Car(),
    7: Buss()
}
CITY_DATA = {
    "name": "Gothenburg",
    "currency": CURRENCY
}
CITY_TOLL_FEE_RATE_DATA = [
   {"start_time": time(6, 0), "end_time": time(6, 29),  "fee": 8 },
   {"start_time": time(6, 30), "end_time": time(6, 59),  "fee": 13 },
   {"start_time": time(7, 0), "end_time": time(7, 59),  "fee": 18 },
   {"start_time": time(8, 0), "end_time": time(8, 29),  "fee": 13 },
   {"start_time": time(8, 30), "end_time": time(14, 59),  "fee": 8 },
   {"start_time": time(15, 0), "end_time": time(15, 29),  "fee": 13 },
   {"start_time": time(15, 30), "end_time": time(16, 29),  "fee": 18 },
   {"start_time": time(17, 0), "end_time": time(17, 59),  "fee": 13 },
   {"start_time": time(18, 0), "end_time": time(18, 29),  "fee": 8 },
   {"start_time": time(18, 30), "end_time": time(5, 59),  "fee": 0 }
]
