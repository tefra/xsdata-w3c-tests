from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[str] = field(
        init=False,
        default_factory=lambda: [
            "abcdefab",
        ],
        metadata={
            "tokens": True,
        }
    )
