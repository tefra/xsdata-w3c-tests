from dataclasses import dataclass, field
from typing import Optional


@dataclass
class B:
    class Meta:
        name = "b"

    a: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    b: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    c: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    one_com_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://one.com/",
            "max_occurs": 2,
            "process_contents": "skip",
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
    f: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 4,
        },
    )
    two_com_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://two.com/",
            "max_occurs": 2,
            "process_contents": "skip",
        },
    )


@dataclass
class Doc(E):
    class Meta:
        name = "doc"
