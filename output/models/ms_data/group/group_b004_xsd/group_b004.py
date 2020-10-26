from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ComplexType:
    """
    :ivar r1:
    :ivar r2:
    :ivar r3:
    """
    class Meta:
        name = "complexType"

    r1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    r2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    r3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
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
