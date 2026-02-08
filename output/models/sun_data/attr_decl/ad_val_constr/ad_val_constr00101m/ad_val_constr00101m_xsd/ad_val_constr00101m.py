from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "AttrDecl/valConstr"


@dataclass(kw_only=True)
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/valConstr"

    number: int = field(
        init=False,
        default=12,
        metadata={
            "type": "Attribute",
            "namespace": "AttrDecl/valConstr",
        },
    )
    price: Decimal = field(
        init=False,
        default=Decimal("12.3"),
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/valConstr"

    element_with_attr: ElementWithAttr = field(
        metadata={
            "name": "elementWithAttr",
            "type": "Element",
        }
    )
