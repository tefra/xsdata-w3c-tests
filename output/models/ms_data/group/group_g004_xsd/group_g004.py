from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
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
