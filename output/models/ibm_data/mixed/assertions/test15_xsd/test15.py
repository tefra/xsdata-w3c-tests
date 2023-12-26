from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class XType:
    class Meta:
        name = "x_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 20,
            "pattern": r"val[1-9][0-9]*",
        },
    )


@dataclass
class Example:
    x: List[XType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    x_count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
