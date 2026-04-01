import sys

import asyncio

from dishka import make_async_container
from src.application.dto.city import City
from src.infrastructure.config.config_loader import load_forward_from_dotenv_file
from src.infrastructure.config.config_storage import Config
from src.application.use_cases.weather_use_case import WeatherUseCase
from src.infrastructure.ioc_container import AioHttpProvider, UseCaseProvider


async def main():
    try:
        city: City = _get_params()
    except ValueError as e:
        print(e)
        return

    container = await setup_dishka()

    async with container() as req:

        use_case = await req.get(WeatherUseCase)
        result = await use_case(city)

    await container.close()
    print(result)


def _get_params():
    if len(sys.argv) < 2:
        raise ValueError("Передай аргумент")

    return City(sys.argv[1])


async def setup_dishka():
    config = load_forward_from_dotenv_file()

    return make_async_container(
        AioHttpProvider(),
        UseCaseProvider(),
        context={Config: config},
    )


if __name__ == "__main__":
    asyncio.run(main())
