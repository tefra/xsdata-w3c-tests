from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class XType:
    class Meta:
        name = "x_Type"

    value: int = field()
    a: str = field(
        metadata={
            "type": "Attribute",
            "max_length": 20,
            "pattern": r"val[1-9][0-9]*",
        }
    )


@dataclass(kw_only=True)
class Example:
    x: list[XType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    x_count: int = field(
        metadata={
            "type": "Attribute",
        }
    )
