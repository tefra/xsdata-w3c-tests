from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComplexType:
    """
    :ivar r1:
    """
    class Meta:
        name = "complexType"

    r1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Elem(ComplexType):
    """
    :ivar a:
    """
    class Meta:
        name = "elem"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


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
