from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "AttrGroup/attrWCard"


@dataclass(kw_only=True)
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrGroup/attrWCard"

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
        },
    )
    height: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrGroup/attrWCard"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
