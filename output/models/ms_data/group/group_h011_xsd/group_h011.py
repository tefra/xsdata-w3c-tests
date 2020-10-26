from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
    """
    :ivar choice:
    """
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "x1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "x2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "y1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "y2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 4,
        }
    )


@dataclass
class Elem(A):
    """
    :ivar x1:
    :ivar x2:
    :ivar y1:
    :ivar y2:
    """
    class Meta:
        name = "elem"

    x1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    x2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    y1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    y2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
