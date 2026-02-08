from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "AttrDecl/type"


@dataclass(kw_only=True)
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/type"

    number: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "AttrDecl/type",
            "min_exclusive": 0,
            "max_exclusive": 13,
        },
    )
    price: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": Decimal("0.0"),
            "max_exclusive": Decimal("13.0"),
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/type"

    element_with_attr: ElementWithAttr = field(
        metadata={
            "name": "elementWithAttr",
            "type": "Element",
        }
    )
