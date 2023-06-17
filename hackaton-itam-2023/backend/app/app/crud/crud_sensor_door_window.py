from typing import List, Any, Dict, Optional, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select

from app.crud.base import CRUDBase
from app.models.sensor_door_window import SensorDoorWindow
from app.schemas.sensor_door_window import SensorDoorWindowCreate, SensorDoorWindowUpdate

class CRUDSensorDoorWindow(CRUDBase[SensorDoorWindow, SensorDoorWindowCreate, SensorDoorWindowUpdate]):
    async def get_by_id(self, db: AsyncSession, *, id: int) -> Optional[SensorDoorWindow]:
        result = await db.execute(select(SensorDoorWindow).filter(SensorDoorWindow.id == id))
        return result.scalars().first()
    
sensor_door_window = CRUDSensorDoorWindow(SensorDoorWindow)