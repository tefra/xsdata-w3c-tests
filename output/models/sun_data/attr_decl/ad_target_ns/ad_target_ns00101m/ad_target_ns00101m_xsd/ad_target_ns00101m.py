from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "AttrDecl/targetNS"


@dataclass
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/targetNS"

    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "AttrDecl/targetNS",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/targetNS"

    element_with_attr: Optional[ElementWithAttr] = field(
        default=None,
        metadata={
            "name": "elementWithAttr",
            "type": "Element",
            "required": True,
        }
    )
