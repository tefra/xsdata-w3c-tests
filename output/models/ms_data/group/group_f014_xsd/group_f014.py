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

    a1: Optional[object] = field(
        default=None,
        metadata={
            "name": "A1",
            "type": "Element",
            "namespace": "",
        }
    )
    a2: Optional[object] = field(
        default=None,
        metadata={
            "name": "A2",
            "type": "Element",
            "namespace": "",
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
