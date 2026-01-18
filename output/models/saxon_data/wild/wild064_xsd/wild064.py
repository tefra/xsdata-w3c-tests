from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class E:
    class Meta:
        name = "e"

    value: Decimal = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class G:
    class Meta:
        name = "g"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Zing:
    class Meta:
        name = "zing"

    e: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    f: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        },
    )


@dataclass(kw_only=True)
class Doc(Zing):
    class Meta:
        name = "doc"
