from typing import Optional, List
from datetime import datetime, time

from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from .config import COUNTRY_TIME_ZONE as _timezone

engine = SQLAlchemy()
ma = Marshmallow()

class Country(engine.Model):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    currency: Mapped[str] = mapped_column(String(10))
    created_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(_timezone))
    updated_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(_timezone))
    
    cities: Mapped[List["City"]] = relationship(
        back_populates="country", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "name": self.name,
            "currency": self.currency,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __repr__(self) -> str:
        return f"Country(name={self.name!r}, currency={self.currency!r})"


class City(engine.Model):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))
    created_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(_timezone))
    updated_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(_timezone))
    
    country: Mapped[List["Country"]] = relationship(
        back_populates="cities"
    )
    toll_fee_rates: Mapped[List["CityTollFeeRate"]] = relationship(
        back_populates="city", cascade="all, delete-orphan"
    )
    vehicle_toll_fees: Mapped[List["VehicleTollFee"]] = relationship(
        back_populates="city", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "name": self.name,
            "country_id": self.country_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __repr__(self) -> str:
        return f"City(name={self.name!r}, country={self.country.name!r})"


class CityTollFeeRate(engine.Model):
    __tablename__ = "city_toll_fee_rate"

    id: Mapped[int] = mapped_column(primary_key=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    start_time: Mapped[time]
    end_time: Mapped[time]
    fee: Mapped[float]
    created_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(_timezone))
    updated_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(_timezone))
    
    city: Mapped["City"] = relationship(back_populates="toll_fee_rates")

    def to_dict(self):
        return {
            "city": self.city.name,
            "start_time": self.start_time.strftime("%I:%M %p"),
            "end_time": self.end_time.strftime("%I:%M %p"),
            "fee": self.fee,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __repr__(self) -> str:
        return f"City(city={self.city.name!r}, start_time={self.start_time!r}, end_time={self.end_time!r}. fee={self.fee!r})"


class VehicleTollFee(engine.Model):
    __tablename__ = "vehicle_toll_fee"

    id: Mapped[int] = mapped_column(primary_key=True)
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    vehicle: Mapped[str] = mapped_column(String(20))
    vehicle_number: Mapped[str] = mapped_column(String(20))
    fee: Mapped[Optional[float]]
    last_charged_at: Mapped[datetime]
    created_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(_timezone))
    updated_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(_timezone))

    city: Mapped["City"] = relationship(back_populates="vehicle_toll_fees")

    def to_dict(self):
        return {
            "city": self.city.name,
            "vehicle": self.vehicle,
            "vehicle_number": self.vehicle_number,
            "fee": self.fee,
            "last_charged_at": self.last_charged_at,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __repr__(self) -> str:
        return f"Toll Fee(city={self.city.name!r}, vehicle_number={self.vehicle_number!r}, fee={self.fee!r})"
