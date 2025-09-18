import pandas as pd
import requests
from abc import ABC, abstractmethod
import logging

class APIClient(ABC):
    @abstractmethod
    def fetch(self, api_key: str, params: dict) -> pd.DataFrame:
        """
        Fetch real-time data from the API endpoint.

        Args:
            - api_key (str): API key provided by client
            - params (dict): parameters for API request

        Returns:
            - data (pd.DataFrame): raw current data
        """
        pass

class AirNowClient(APIClient):
    BASE_URL = "https://www.airnowapi.org/aq/observation/zipCode/current/"

    def fetch(self, api_key: str, params: dict) -> pd.DataFrame:
        try: 
            params["API_KEY"] = api_key
            response = requests.get(self.BASE_URL, params=params)
            raw = response.json()
            data = pd.DataFrame(raw)
            return data
        except Exception as e:
            logging.error(f"AirNow API request failed: {e}", exc_info=True)
            raise e


class OpenWeatherClient(APIClient):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def fetch(self, api_key: str, params: dict) -> pd.DataFrame:
        try: 
            params["appid"] = api_key
            response = requests.get(self.BASE_URL, params=params)
            raw = response.json()
            data = pd.json_normalize(raw)
            return data
        except Exception as e:
            logging.error(f"OpenWeather API request failed: {e}", exc_info=True)
            raise e

class GoogleMapsClient(APIClient):
    BASE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

    def fetch(self, api_key: str, params: dict) -> pd.DataFrame:
        try: 
            params["key"] = api_key
            response = requests.get(self.BASE_URL, params=params)
            raw = response.json()
            data = pd.DataFrame(raw)
            return data
        except Exception as e:
            logging.error(f"GoogleMaps API request failed: {e}", exc_info=True)
            raise e