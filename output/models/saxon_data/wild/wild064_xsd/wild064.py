from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class E:
    class Meta:
        name = "e"

    value: Optional[Decimal] = field(
        default=None
    )


@dataclass
class G:
    class Meta:
        name = "g"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class Zing:
    class Meta:
        name = "zing"

    e: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    f: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "required": True,
        }
    )


@dataclass
class Doc(Zing):
    class Meta:
        name = "doc"
