


from dataclasses import dataclass



@dataclass(slots=True, frozen=True)
class Weather:
    temperature: float
    description: str




