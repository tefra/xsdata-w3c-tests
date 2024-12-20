from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Para:
    class Meta:
        name = "para"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ref: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
