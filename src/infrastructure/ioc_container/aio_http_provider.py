from collections.abc import AsyncGenerator
from typing import Any
from aiohttp import ClientSession

from dishka import Provider, from_context, Scope, provide

from src.application.interfaces.external_requests.openweather import OpenWeather
from src.infrastructure.config.config_loader import Config
from src.infrastructure.external_requests.openweather import ImplOpenWeather


class AioHttpProvider(Provider):
    context = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.REQUEST)
    async def get_aiohttp_session(
            self
    ) -> AsyncGenerator[ClientSession, Any]:
        async with ClientSession() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    async def get_openweather(self, session: ClientSession, config: Config) -> OpenWeather:
        return ImplOpenWeather(session, api_key=config.openweather_api_key)
