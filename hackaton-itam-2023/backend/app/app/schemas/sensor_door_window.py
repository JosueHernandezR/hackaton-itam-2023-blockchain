from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class SensorDoorWindowBase(BaseModel):
    pass

class SensorDoorWindowCreate(SensorDoorWindowBase):
    id_sensor: str
    battery: int
    contact: bool
    device_temperature: int
    linkquality: int
    power_outage_count: int
    voltage: int

class SensorDoorWindowUpdate(SensorDoorWindowBase):
    pass

class SensorDoorWindowInDBBase(SensorDoorWindowBase):
    id: int
    id_sensor: str
    battery: int
    contact: bool
    device_temperature: int
    linkquality: int
    power_outage_count: int
    voltage: int
    created_data: datetime

    class Config:
        orm_mode = True

class SensorDoorWindow(SensorDoorWindowInDBBase):
    pass

class SensorDoorWindowInDB(SensorDoorWindowInDBBase):
    pass