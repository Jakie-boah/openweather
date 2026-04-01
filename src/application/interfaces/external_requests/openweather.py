from typing import Protocol
from abc import abstractmethod

from src.application.dto.weather import Weather
from src.application.dto.city import City


class OpenWeather(Protocol):
    @abstractmethod
    async def get_current_weather(self, city: City) -> Weather: ...
