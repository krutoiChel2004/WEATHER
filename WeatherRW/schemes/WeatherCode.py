from enum import Enum

class WeatherCode(Enum):
    CLEAR_SKY = 0
    MAINLY_CLEAR = 1
    PARTLY_CLOUDY = 2
    OVERCAST = 3
    FOG = 45
    DEPOSITING_RIME_FOG = 48
    DRIZZLE_LIGHT = 51
    DRIZZLE_MODERATE = 53
    DRIZZLE_DENSE = 55
    FREEZING_DRIZZLE_LIGHT = 56
    FREEZING_DRIZZLE_DENSE = 57
    RAIN_SLIGHT = 61
    RAIN_MODERATE = 63
    RAIN_HEAVY = 65
    FREEZING_RAIN_LIGHT = 66
    FREEZING_RAIN_HEAVY = 67
    SNOW_SLIGHT = 71
    SNOW_MODERATE = 73
    SNOW_HEAVY = 75
    SNOW_GRAINS = 77
    RAIN_SHOWERS_SLIGHT = 80
    RAIN_SHOWERS_MODERATE = 81
    RAIN_SHOWERS_VIOLENT = 82
    SNOW_SHOWERS_SLIGHT = 85
    SNOW_SHOWERS_HEAVY = 86
    THUNDERSTORM_SLIGHT = 95
    THUNDERSTORM_WITH_HAIL_SLIGHT = 96
    THUNDERSTORM_WITH_HAIL_HEAVY = 99

    @classmethod
    def description(cls, code: int) -> str:
        descriptions = {
            cls.CLEAR_SKY: "Clear sky",
            cls.MAINLY_CLEAR: "Mainly clear",
            cls.PARTLY_CLOUDY: "Partly cloudy",
            cls.OVERCAST: "Overcast",
            cls.FOG: "Fog",
            cls.DEPOSITING_RIME_FOG: "Depositing rime fog",
            cls.DRIZZLE_LIGHT: "Drizzle: Light intensity",
            cls.DRIZZLE_MODERATE: "Drizzle: Moderate intensity",
            cls.DRIZZLE_DENSE: "Drizzle: Dense intensity",
            cls.FREEZING_DRIZZLE_LIGHT: "Freezing Drizzle: Light intensity",
            cls.FREEZING_DRIZZLE_DENSE: "Freezing Drizzle: Dense intensity",
            cls.RAIN_SLIGHT: "Rain: Slight intensity",
            cls.RAIN_MODERATE: "Rain: Moderate intensity",
            cls.RAIN_HEAVY: "Rain: Heavy intensity",
            cls.FREEZING_RAIN_LIGHT: "Freezing Rain: Light intensity",
            cls.FREEZING_RAIN_HEAVY: "Freezing Rain: Heavy intensity",
            cls.SNOW_SLIGHT: "Snow fall: Slight intensity",
            cls.SNOW_MODERATE: "Snow fall: Moderate intensity",
            cls.SNOW_HEAVY: "Snow fall: Heavy intensity",
            cls.SNOW_GRAINS: "Snow grains",
            cls.RAIN_SHOWERS_SLIGHT: "Rain showers: Slight intensity",
            cls.RAIN_SHOWERS_MODERATE: "Rain showers: Moderate intensity",
            cls.RAIN_SHOWERS_VIOLENT: "Rain showers: Violent intensity",
            cls.SNOW_SHOWERS_SLIGHT: "Snow showers: Slight intensity",
            cls.SNOW_SHOWERS_HEAVY: "Snow showers: Heavy intensity",
            cls.THUNDERSTORM_SLIGHT: "Thunderstorm: Slight or moderate",
            cls.THUNDERSTORM_WITH_HAIL_SLIGHT: "Thunderstorm with slight hail",
            cls.THUNDERSTORM_WITH_HAIL_HEAVY: "Thunderstorm with heavy hail",
        }
        return descriptions.get(cls(code), "Unknown weather condition")