from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ComplexType:
    """
    :ivar r1:
    :ivar r2:
    """
    class Meta:
        name = "complexType"

    r1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    r2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 100,
            "sequential": True,
        }
    )


@dataclass
class Elem(ComplexType):
    class Meta:
        name = "elem"


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
