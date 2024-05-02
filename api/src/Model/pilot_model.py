from dataclasses import dataclass


@dataclass
class PilotModel:
    id: int = 0
    name: str = ''
    team: str = ''
    gpwin: int = 0
    gpmade: int = 0
    points: float = 0
    fastestlap: int = 0
    podiums: int = 0
    pole: int = 0