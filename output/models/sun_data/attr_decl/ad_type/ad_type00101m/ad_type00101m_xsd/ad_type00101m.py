from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "AttrDecl/type"


@dataclass
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/type"

    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "AttrDecl/type",
        },
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/type"

    element_with_attr: Optional[ElementWithAttr] = field(
        default=None,
        metadata={
            "name": "elementWithAttr",
            "type": "Element",
            "required": True,
        },
    )
