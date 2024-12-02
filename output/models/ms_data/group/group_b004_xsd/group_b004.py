from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComplexType:
    class Meta:
        name = "complexType"

    r1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    r2: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 4,
            "sequence": 1,
        },
    )
    r3: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass
class Elem(ComplexType):
    class Meta:
        name = "elem"


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
