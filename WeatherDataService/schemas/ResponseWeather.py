from pydantic import BaseModel

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ResponseWeather(BaseModel):
    temperature: float
    weather_code_description: Optional[str] = None
    precipitation: float
    surface_pressure: float
    wind_speed_10m: float
    wind_direction_10m: float
    wind_direction_description: Optional[str] = None
    time_moscow: datetime