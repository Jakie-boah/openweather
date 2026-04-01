from src.application.dto.city import City
from src.application.interfaces.external_requests.openweather import OpenWeather
from aiohttp.client_exceptions import ClientResponseError


class WeatherUseCase:
    def __init__(self, openweather: OpenWeather):
        self.openweather = openweather

    async def __call__(self, city: City):
        try:
            weather = await self.openweather.get_current_weather(city)

        except ClientResponseError:
            return f"Unknown city: {city.value}"

        else:
            return f"{city.value}: {weather.description} - {weather.temperature}C"
