from dataclasses import dataclass, field
from typing import Optional


@dataclass
class XType:
    class Meta:
        name = "X_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    a: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Example:
    x: list[XType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
