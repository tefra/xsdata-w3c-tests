from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "AttrGroup/attrUse"


@dataclass(kw_only=True)
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrGroup/attrUse"

    good: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    number: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "AttrGroup/attrUse",
        },
    )
    height: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrGroup/attrUse"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
