from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/name"

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
            "namespace": "AttrDecl/name",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    element_with_attr: Optional[ElementWithAttr] = field(
        default=None,
        metadata={
            "name": "elementWithAttr",
            "type": "Element",
            "required": True,
        }
    )
