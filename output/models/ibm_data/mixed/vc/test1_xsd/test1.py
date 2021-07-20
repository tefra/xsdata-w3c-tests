from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    class Meta:
        name = "test"

    value: Optional[int] = field(
        default=None
    )
