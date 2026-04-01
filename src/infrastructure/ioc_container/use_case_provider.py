from dishka import Scope, provide, Provider

from src.application.use_cases.weather_use_case import WeatherUseCase


class UseCaseProvider(Provider):
    openweather_use_case = provide(WeatherUseCase, scope=Scope.REQUEST)
