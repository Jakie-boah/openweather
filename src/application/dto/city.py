from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class City:
    value: str
