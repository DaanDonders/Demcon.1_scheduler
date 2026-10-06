from dataclasses import dataclass

@dataclass
class Show:
    name: str
    start_time: int
    end_time: int
    stage_number: int | None = None