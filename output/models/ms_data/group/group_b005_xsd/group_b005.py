from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ComplexType:
    """
    :ivar r1_or_r2:
    """
    class Meta:
        name = "complexType"

    r1_or_r2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "r1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "r2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 100,
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
