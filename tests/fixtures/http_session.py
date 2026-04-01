import pytest_asyncio
from aiohttp import ClientSession
from src.infrastructure.external_requests.openweather import ImplOpenWeather


@pytest_asyncio.fixture
async def http_session():
    async with ClientSession() as session:
        yield session


@pytest_asyncio.fixture
async def openweather_service(http_session, config):
    return ImplOpenWeather(http_session, config.openweather_api_key)
