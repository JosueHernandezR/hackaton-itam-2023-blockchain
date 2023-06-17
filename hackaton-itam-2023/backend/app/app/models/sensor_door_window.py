from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import Column, ForeignKey,DateTime, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class SensorDoorWindow(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    id_sensor: str = Column(String, index=True)
    battery: int = Column(Integer)
    contact: bool = Column(Boolean)
    device_temperature: int = Column(Integer)
    linkquality: int = Column(Integer)
    power_outage_count: int = Column(Integer)
    voltage: int = Column(Integer)
    created_data: datetime = Column(DateTime, default=datetime.utcnow())
    