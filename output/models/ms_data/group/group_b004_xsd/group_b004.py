from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ComplexType:
    class Meta:
        name = "complexType"

    r1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 3,
        }
    )
    r2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 4,
            "sequence": 3,
        }
    )
    r3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 3,
        }
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
        }
    )
