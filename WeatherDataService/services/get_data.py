from sqlalchemy.orm import Session
from models.WeatherModel import Weather
from schemas.ResponseWeather import ResponseWeather
from datetime import date, datetime, timedelta

def get_weather_log(date_s: str, db: Session):
    date_list = date_s.split("/")
    date_form = date(year=int(date_list[2]), month=int(date_list[1]), day=int(date_list[0]))
    
    
    start_of_day = datetime.combine(date_form, datetime.min.time())
    end_of_day = start_of_day + timedelta(days=1) 

    weather_data = db.query(Weather).where(Weather.time_moscow >= start_of_day, Weather.time_moscow < end_of_day).all()

    result = [
        ResponseWeather(
            temperature=w.temperature,
            weather_code_description=w.weather_code_description,
            precipitation=w.precipitation,
            surface_pressure=w.surface_pressure,
            wind_speed_10m=w.wind_speed_10m,
            wind_direction_10m=w.wind_direction_10m,
            wind_direction_description=w.wind_direction_description,
            time_moscow=w.time_moscow
        )
        for w in weather_data
    ]

    return result
