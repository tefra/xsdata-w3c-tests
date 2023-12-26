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
            "max_occurs": 5,
        },
    )
    c: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    one_com_element: List[object] = field(
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
    f: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 4,
        },
    )
    two_com_element: List[object] = field(
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
