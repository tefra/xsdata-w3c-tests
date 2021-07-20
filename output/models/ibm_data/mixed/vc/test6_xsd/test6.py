from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Example:
    value: Optional[int] = field(
        default=None
    )
