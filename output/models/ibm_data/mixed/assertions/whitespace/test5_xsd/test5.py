from dataclasses import dataclass, field
from typing import Optional


@dataclass
class X:
    class Meta:
        name = "x"

    value: Optional[str] = field(
        default=None,
    )
