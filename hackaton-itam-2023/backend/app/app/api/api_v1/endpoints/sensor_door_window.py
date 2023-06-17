from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.SensorDoorWindow])
async def read_all_data_for_all_sensors(
    db: AsyncSession = Depends(deps.async_get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    data = await crud.sensor_door_window.get_multi(db=db, skip=skip, limit=limit)
    return data

@router.post("/", response_model=schemas.SensorDoorWindow)
async def create_sensor_door_window_data(
    *,
    db: AsyncSession = Depends(deps.async_get_db),
    data_in: schemas.SensorDoorWindowCreate,
) -> Any:
    data = await crud.sensor_door_window.create(db=db, obj_in=data_in)
    return data