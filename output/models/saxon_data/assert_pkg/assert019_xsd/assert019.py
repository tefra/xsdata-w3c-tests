from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class DatedEvent:
    class Meta:
        name = "datedEvent"

    d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Temp:
    class Meta:
        name = "temp"

    d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    temp: List[Temp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
