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
        },
    )
    price: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
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
