from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
    class Meta:
        name = "a"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class B:
    class Meta:
        name = "b"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    a: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    b: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 3,
            "sequential": True,
        }
    )


@dataclass
class E:
    class Meta:
        name = "e"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
