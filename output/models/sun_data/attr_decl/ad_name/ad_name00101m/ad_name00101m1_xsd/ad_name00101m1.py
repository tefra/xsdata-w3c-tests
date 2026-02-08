from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/name"

    number: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    price: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "AttrDecl/name",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    element_with_attr: ElementWithAttr = field(
        metadata={
            "name": "elementWithAttr",
            "type": "Element",
        }
    )
