from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class XDecimal:
    class Meta:
        name = "X_Decimal"

    value: Decimal = field()
    kind: str = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class XInt:
    class Meta:
        name = "X_Int"

    value: int = field()
    kind: str = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class XString:
    class Meta:
        name = "X_String"

    value: str = field(default="")
    kind: str = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class Example:
    x: list[XInt | XDecimal | XString] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
