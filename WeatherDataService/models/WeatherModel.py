from sqlalchemy import (Column, 
                        Integer,
                        Float, 
                        String, 
                        DateTime)

from database import Base



class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float, nullable=False)
    weather_code_description = Column(String, nullable=False)
    precipitation = Column(Float, nullable=False)
    surface_pressure = Column(Float, nullable=False)
    wind_speed_10m = Column(Float, nullable=False)
    wind_direction_10m = Column(Float, nullable=False)
    wind_direction_description = Column(String, nullable=False)
    time_moscow = Column(DateTime, nullable=False)


