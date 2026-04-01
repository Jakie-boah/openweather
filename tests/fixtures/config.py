import pytest

from src.infrastructure.config.config_loader import load_forward_from_dotenv_file
from src.infrastructure.config.config_storage import Config


@pytest.fixture(scope="session")
def config() -> Config:
    return load_forward_from_dotenv_file()
