from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime, timezone


class Base(DeclarativeBase):
    pass


class TollFee(Base):
    __tablename__ = "toll_fee"

    id: Mapped[int] = mapped_column(primary_key=True)
    vehicle: Mapped[str] = mapped_column(String(10))
    vehicle_number: Mapped[str] = mapped_column(String(20))
    fee: Mapped[Optional[float]]
    created_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"Toll Fee(vehicle_number={self.vehicle_number!r}, fee={self.fee!r})"