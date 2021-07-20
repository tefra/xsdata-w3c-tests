from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "AttrGroup/name"


@dataclass
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrGroup/name"

    good: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrGroup/name"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
