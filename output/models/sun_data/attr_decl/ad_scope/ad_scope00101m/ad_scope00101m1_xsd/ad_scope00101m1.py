from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "AttrDecl/scope"


@dataclass(kw_only=True)
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/scope"

    number: int = field(
        metadata={
            "type": "Attribute",
            "namespace": "AttrDecl/scope",
        }
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
        namespace = "AttrDecl/scope"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
