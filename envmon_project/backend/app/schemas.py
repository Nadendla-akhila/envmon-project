from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReadingCreate(BaseModel):
    sensor_id: str
    timestamp: Optional[datetime]
    pm25: Optional[float]
    pm10: Optional[float]
    no2: Optional[float]
    so2: Optional[float]
    o3: Optional[float]
    co: Optional[float]
    temperature: Optional[float]
    humidity: Optional[float]

class Reading(BaseModel):
    id: int
    sensor_id: str
    timestamp: datetime
    pm25: Optional[float]
    pm10: Optional[float]

    class Config:
        orm_mode = True
