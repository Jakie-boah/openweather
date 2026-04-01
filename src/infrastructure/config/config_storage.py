from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Config:
    openweather_api_key: str
