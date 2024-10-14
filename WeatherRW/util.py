def wind_direction_calculation(wind_direction: float) -> str:
    wind_direction_text = ''
    if wind_direction is not None:
        if 337.5 <= wind_direction <= 360 or 0 <= wind_direction < 22.5:
            wind_direction_text = 'N'
        elif 22.5 <= wind_direction < 67.5:
            wind_direction_text = 'NE'
        elif 67.5 <= wind_direction < 112.5:
            wind_direction_text = 'E'
        elif 112.5 <= wind_direction < 157.5:
            wind_direction_text = 'SE'
        elif 157.5 <= wind_direction < 202.5:
            wind_direction_text = 'S'
        elif 202.5 <= wind_direction < 247.5:
            wind_direction_text = 'SW'
        elif 247.5 <= wind_direction < 292.5:
            wind_direction_text = 'W'
        elif 292.5 <= wind_direction < 337.5:
            wind_direction_text = 'NW'

    return wind_direction_text
