from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Temp:
    class Meta:
        name = "temp"

    value: Optional[str] = field(
        default=None,
    )
