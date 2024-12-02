from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Inner:
    class Meta:
        name = "inner"

    a: list["Inner.A"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 4,
        },
    )
    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class A:
        b: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 4,
            },
        )


@dataclass
class Outer:
    class Meta:
        name = "outer"

    inner: list[Inner] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
