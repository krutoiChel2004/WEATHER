from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session

from database import get_db

from services.get_data import (get_weather_log, get_weather_log_file)


router = APIRouter(
    prefix="/data",
    tags=["DATA"]
)

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/")
async def weather_log(date_start: str, date_end: str, db: db_dependency):
    return get_weather_log(date_start, date_end, db)

@router.get("/file")
async def weather_log_file(date_start: str, date_end: str, db: db_dependency):
    return get_weather_log_file(date_start, date_end, db)