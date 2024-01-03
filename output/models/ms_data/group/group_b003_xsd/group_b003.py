from dataclasses import dataclass, field
from typing import Optional, Any


@dataclass
class ComplexType:
    class Meta:
        name = "complexType"

    r1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    r2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    r3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    r4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Elem(ComplexType):
    class Meta:
        name = "elem"

    r3: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    r4: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
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
