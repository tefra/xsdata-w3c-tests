from dataclasses import dataclass, field
from typing import Optional


@dataclass
class X:
    class Meta:
        name = "x"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
