from dataclasses import dataclass, field
from typing import Optional


@dataclass
class B:
    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Elem(B):
    class Meta:
        name = "elem"

    a1_or_a2: Optional[object] = field(
        default=None,
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
        }
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
        }
    )
