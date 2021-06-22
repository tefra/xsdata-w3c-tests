from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Elem:
    class Meta:
        name = "elem"

    value: Optional[str] = field(
        default=None,
        metadata={
            "white_space": "collapse",
            "pattern": r"Hello world",
        }
    )
