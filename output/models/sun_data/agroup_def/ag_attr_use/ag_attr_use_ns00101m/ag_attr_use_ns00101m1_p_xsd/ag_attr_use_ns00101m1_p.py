from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "AttrGroup/attrUse"


@dataclass
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrGroup/attrUse"

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
            "namespace": "AttrGroup/attrUse",
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
        namespace = "AttrGroup/attrUse"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
