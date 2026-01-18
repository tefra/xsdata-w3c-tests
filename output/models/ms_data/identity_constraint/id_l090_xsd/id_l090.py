from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class U:
    class Meta:
        name = "u"
        namespace = "myNS.tempuri.org"

    value: Decimal = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t_or_u: list[T | U] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "t",
                    "type": T,
                },
                {
                    "name": "u",
                    "type": U,
                },
            ),
        },
    )
