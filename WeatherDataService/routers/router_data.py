from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session

from database import get_db

from services.get_data import get_weather_log


router = APIRouter(
    prefix="/data",
    tags=["DATA"]
)

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/")
async def weather_log(date: str, db: db_dependency):
    return get_weather_log(date, db)
