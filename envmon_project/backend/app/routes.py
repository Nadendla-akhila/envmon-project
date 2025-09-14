from fastapi import APIRouter, Depends, HTTPException, Header
from typing import List
from . import schemas, crud
from .database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
import os

API_KEY = os.getenv('SENSOR_API_KEY')

router = APIRouter(prefix='/api')

@router.post('/readings', response_model=schemas.Reading)
async def ingest_reading(reading: schemas.ReadingCreate, x_api_key: str = Header(None), db: AsyncSession = Depends(get_db)):
    if API_KEY and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail='Invalid API key')
    data = reading.dict()
    data = {k: v for k, v in data.items() if v is not None}
    created = await crud.create_reading(db, data)
    # simple threshold alerting (example): when PM2.5 > 100
    try:
        if getattr(created, 'pm25', 0) and created.pm25 > 100:
            print(f'ALERT: High PM2.5 from {created.sensor_id}: {created.pm25}')
    except Exception:
        pass
    return created

@router.get('/readings', response_model=List[schemas.Reading])
async def list_readings(limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud.get_recent_readings(db, limit)
