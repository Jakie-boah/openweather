import pytest

from src.application.dto.city import City
from src.application.dto.weather import Weather
from aiohttp.client_exceptions import ClientResponseError


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "city",
    (City("Moscow"), City("blablabla"))
)
async def test_openweather(openweather_service, city):
    if city.value == "Moscow":
        result = await openweather_service.get_current_weather(city)
        assert isinstance(result, Weather)

    else:
        with pytest.raises(ClientResponseError):
            await openweather_service.get_current_weather(city)
