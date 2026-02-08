from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "AttrDecl/targetNS"


@dataclass(kw_only=True)
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/targetNS"

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
            "namespace": "AttrDecl/targetNS",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/targetNS"

    element_with_attr: ElementWithAttr = field(
        metadata={
            "name": "elementWithAttr",
            "type": "Element",
        }
    )
