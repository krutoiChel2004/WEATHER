from util import wind_direction_calculation
from schemes.WeatherCode import WeatherCode
from models.WeatherModel import Weather
from WeatherReader import WeatherReader

import time

from database import engine, Base, SessionLocal

Base.metadata.create_all(bind=engine)

url = "https://api.open-meteo.com/v1/forecast"

params = {
	"latitude": 55.69,
	"longitude": 37.35,
	"current": ["temperature_2m", 
                "precipitation", 
                "weather_code", 
                "surface_pressure", 
                "wind_speed_10m", 
                "wind_direction_10m"],
	"wind_speed_unit": "ms",
	"timezone": "Europe/Moscow",
	"timeformat": "unixtime",
}

reader = WeatherReader(url, params)

n = 30  # интервал в секундах
start_time = time.perf_counter()

if __name__ == "__main__":
    while True:
        db = SessionLocal()

        weather = reader.weather_read()

        w = Weather(temperature=weather["temperature_2m"],
                    weather_code_description=WeatherCode.description(weather["weather_code"]),
                    precipitation=weather["precipitation"],
                    surface_pressure=weather["surface_pressure"],
                    wind_speed_10m=weather["wind_speed_10m"],
                    wind_direction_10m=weather["wind_direction_10m"],
                    wind_direction_description=wind_direction_calculation(weather["wind_direction_10m"]),
                    time_moscow=weather["date_time"])
        

        db.add(w)
        db.commit()
        db.refresh(w)
        db.close()

        elapsed_time = time.perf_counter() - start_time
        
        # Засыпаем ровно до следующего выполнения
        time.sleep(max(0, n - elapsed_time))
        
        # Обновляем время старта
        start_time = time.perf_counter()