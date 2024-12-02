from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Element1:
    class Meta:
        name = "element1"

    attribute1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(あ|ｱ)*",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    element1: list[Element1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
