from dataclasses import dataclass, field
from typing import List


@dataclass
class Example:
    value: List[int] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
