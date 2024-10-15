from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session
from models.WeatherModel import Weather
from schemas.ResponseWeather import ResponseWeather
from datetime import date, datetime
import pandas as pd
from io import BytesIO

def get_weather_log(date_start: str, date_end: str, db: Session):
    date_list_start = date_start.split("/")
    date_form_start = date(year=int(date_list_start[2]), month=int(date_list_start[1]), day=int(date_list_start[0]))

    date_list_end = date_end.split("/")
    date_form_end = date(year=int(date_list_end[2]), month=int(date_list_end[1]), day=int(date_list_end[0]))
    
    
    start_of_day = datetime.combine(date_form_start, datetime.min.time())
    end_of_day = datetime.combine(date_form_end, datetime.max.time())

    weather_data = db.query(Weather).where(Weather.time_moscow >= start_of_day, Weather.time_moscow <= end_of_day).all()

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


def get_weather_log_file(date_start: str, date_end: str, db: Session):

    result = get_weather_log(date_start, date_end, db)

    result_dicts = [w.dict() for w in result]

    # Создаем DataFrame из списка словарей
    df = pd.DataFrame(result_dicts)
    print(df)

    output = BytesIO()

    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
       df.to_excel(writer, sheet_name='Weather Data')

    output.seek(0)

    return StreamingResponse(output, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 
                             headers={"Content-Disposition": f"attachment; filename={date_start}-{date_end}.xlsx"})