from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, Optional

__NAMESPACE__ = "AttrGroup/attrWCard"


@dataclass
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrGroup/attrWCard"

    good: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrGroup/attrWCard"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
