import os

from dotenv import load_dotenv

from src.infrastructure.config.config_storage import Config


def _load_config_from_env() -> Config:
    return Config(
        openweather_api_key=os.environ["OPENWEATHER_API_KEY"],
    )


def load_forward_from_dotenv_file() -> Config:
    load_dotenv()
    return _load_config_from_env()
