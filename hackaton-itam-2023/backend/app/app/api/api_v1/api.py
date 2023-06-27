from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils
from app.api.api_v1.endpoints import sensor_door_window, control_lights
api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(sensor_door_window.router, prefix="/sensor_door_window", tags=["sensor_door_window"])
api_router.include_router(control_lights.router, prefix="/control", tags=["control"])