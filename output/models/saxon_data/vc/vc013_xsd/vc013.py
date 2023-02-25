from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Temp:
    class Meta:
        name = "temp"

    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
