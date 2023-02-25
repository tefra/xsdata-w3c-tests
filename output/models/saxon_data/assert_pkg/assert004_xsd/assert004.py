from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Inner:
    class Meta:
        name = "inner"

    a: List["Inner.A"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 4,
        }
    )
    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class A:
        b: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 4,
            }
        )


@dataclass
class Outer:
    class Meta:
        name = "outer"

    inner: List[Inner] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
