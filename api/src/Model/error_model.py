from dataclasses import dataclass
@dataclass
class ErrorModel:
    message: str
    status: int
