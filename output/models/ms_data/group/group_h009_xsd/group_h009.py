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
        }
    )


@dataclass
class Elem(A):
    """
    :ivar choice:
    """
    class Meta:
        name = "elem"

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
            "max_occurs": 999999999999999,
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
