from aiohttp import ClientSession
from src.application.dto.city import City
from src.application.dto.weather import Weather
from src.application.interfaces.external_requests.openweather import OpenWeather


class ImplOpenWeather(OpenWeather):
    def __init__(self, session: ClientSession, api_key: str):
        self.session = session
        self.__api_key = api_key

    async def get_current_weather(self, city: City) -> Weather:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city.value,
            "appid": self.__api_key,
            "lang": "ru",
            "units": "metric"
        }

        async with self.session.request(
                "GET", url, params=params, timeout=10
        ) as resp:
            resp.raise_for_status()

            result = await resp.json()

            weather = Weather(
                temperature=result["main"]["temp"],
                description=result["weather"][0]["description"],
            )

            return weather
