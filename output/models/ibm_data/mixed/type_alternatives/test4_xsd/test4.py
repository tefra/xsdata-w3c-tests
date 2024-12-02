from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Example:
    x: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
