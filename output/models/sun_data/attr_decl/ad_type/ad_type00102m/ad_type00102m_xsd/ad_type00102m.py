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
            "min_exclusive": 0,
            "max_exclusive": 13,
        },
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": Decimal("0.0"),
            "max_exclusive": Decimal("13.0"),
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
