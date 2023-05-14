from dataclasses import dataclass, field
from typing import List


@dataclass
class A:
    class Meta:
        name = "a"

    value: str = field(
        init=False,
        default="e1",
        metadata={
            "required": True,
        }
    )


@dataclass
class B:
    class Meta:
        name = "b"

    value: str = field(
        init=False,
        default="e1",
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
            "sequence": 1,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequence": 1,
        }
    )
    b: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 6,
            "sequence": 1,
        }
    )


@dataclass
class E:
    class Meta:
        name = "e"

    value: str = field(
        init=False,
        default="e1",
        metadata={
            "required": True,
        }
    )
