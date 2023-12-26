from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Elem(B):
    class Meta:
        name = "elem"

    a1_or_a2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "A1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "A2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        },
    )


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
