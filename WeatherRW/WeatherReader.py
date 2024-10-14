import openmeteo_requests
from pytz import timezone
from datetime import datetime

class WeatherReader:
    def __init__(self, url: str, params:dict):
        self.url: str = url
        self.params: dict = params
        self.__om = openmeteo_requests.Client()

    def weather_read(self) -> dict:
        weather_dict = {}

        responses = self.__om.weather_api(self.url, params=self.params)
        response = responses[0]
        current = response.Current()

        time_utc = datetime.utcfromtimestamp(current.Time() + response.UtcOffsetSeconds())
        moscow_tz = timezone('Europe/Moscow')
        time_moscow = time_utc.astimezone(moscow_tz)
        weather_dict["date_time"] = time_moscow

        for idx, param in enumerate(self.params["current"]):
            weather_dict[param] = current.Variables(idx).Value()

        return weather_dict