import pandas as pd
import requests
from abc import ABC, abstractmethod
from datetime import datetime as dt
import logging

from sqlalchemy.util import dataclass_fields
from src.data_ingestion import IngestAQIData, IngestWeatherData, IngestMapsData

class DataStrategy(ABC):
    """
    Abstract class defining strategy for handling data
    """
    @abstractmethod
    def handle_data(self) -> pd.DataFrame: 
        pass

class AQIPreprocessStrategy(DataStrategy):
    """
    Preprocessing strategy for historical AQI data
    """
    def handle_data(self) -> pd.DataFrame:
        """
        Returns: 
            - data (pd.DataFrame): historic data for daily San Francisco AQI
        """
        try:
            # Ingesting data 
            data = IngestAQIData().get_data()
            # Only selecting observations from the past two years
            data["date"] = pd.to_datetime(data["date"])
            data = data[data["date"] >= "2023-09-03"]
            data.sort_values("date", inplace=True)
            # Calculating AQI as the max air pollutant value
            data['AQI'] = data[[' pm25', ' pm10', ' o3', ' no2', ' so2', ' co']].max(axis=1)
            data = data.drop([' pm25', ' pm10', ' o3', ' no2', ' so2', ' co'], axis=1)

            return data

        except Exception as e:
            logging.error(f"Failed to preprocess historic AQI data: {e}")
            raise

class WeatherPreprocessStrategy(DataStrategy):
    """
    Preprocessing strategy for historical weather data.
    """
    def handle_data(self) -> pd.DataFrame:
        """
        Returns: 
            - data (pd.DataFrame): historic data for daily San Francisco weather
        """
        try:
            # Ingesting data
            data = IngestWeatherData().get_data()
            # Only selecting relevant columns
            cols = ["dt", "temp", "feels_like", "temp_min", "temp_max", "pressure", "humidity", 
                    "wind_speed", "wind_deg", "wind_gust", "clouds_all"]
            data = data[cols]
            # Only selecting observations from the past two years
            date = dt.strptime("09-13-2023", "%m-%d-%Y").timestamp()
            data = data[data["dt"] >= date]
            data.sort_values("dt", inplace=True)
            # Imputing null values
            data["wind_gust"] = data["wind_gust"].fillna(0)

            return data

        except Exception as e:
            logging.error(f"Failed to preprocess historic weather data: {e}")
            raise