from sqlalchemy import select
from .models import SensorReading

async def create_reading(db, reading_data):
    reading = SensorReading(**reading_data)
    db.add(reading)
    await db.commit()
    await db.refresh(reading)
    return reading

async def get_recent_readings(db, limit: int = 100):
    result = await db.execute(select(SensorReading).order_by(SensorReading.timestamp.desc()).limit(limit))
    return result.scalars().all()
