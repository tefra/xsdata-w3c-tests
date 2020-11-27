from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Temp:
    class Meta:
        name = "temp"

    value: Optional[str] = field(
        default=None,
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Attribute",
            "required": True,
        }
    )
