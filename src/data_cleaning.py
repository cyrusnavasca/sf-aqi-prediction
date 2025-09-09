import pandas as pd
import requests
from abc import ABC, abstractmethod
import logging

class DataStrategy(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def handle_data(self): #todo: define output type
        pass

class AQIPreprocessStrategy(DataStrategy):
    def __init__(self) -> None:
        pass

    def handle_data(self) -> pd.DataFrame:
        pass #todo