from dataclasses import dataclass, field
from typing import Optional


@dataclass
class B:
    e: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Abc(B):
    class Meta:
        name = "abc"

    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Doc(Abc):
    class Meta:
        name = "doc"
