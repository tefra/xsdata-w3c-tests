from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    class Meta:
        name = "b"

    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    b: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    c: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
        },
    )
    d: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class E(B):
    class Meta:
        name = "e"

    e: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    f: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 3,
            "max_occurs": 4,
        },
    )
    g: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 4,
        },
    )


@dataclass
class Doc(E):
    class Meta:
        name = "doc"
