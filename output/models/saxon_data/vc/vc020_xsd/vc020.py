from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Temp:
    """
    :ivar x:
    :ivar y:
    """
    class Meta:
        name = "temp"

    x: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
