import pytest

from src.application.use_cases.weather_use_case import WeatherUseCase
from src.application.dto.city import City


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "city",
    (City("Moscow"), City("Moscowblablalbal"))
)
async def test_get_weather_use_case(openweather_service, city):
    use_case = WeatherUseCase(openweather_service)
    result = await use_case(city)

    if not city.value == "Moscow":
        assert result == f"Unknown city: {city.value}"
    else:
        assert f"{city.value}:" in result
