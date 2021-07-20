from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "AttrDecl/valConstr"


@dataclass
class ElementWithAttr:
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/valConstr"

    number: int = field(
        init=False,
        default=12,
        metadata={
            "type": "Attribute",
            "namespace": "AttrDecl/valConstr",
        }
    )
    price: Decimal = field(
        init=False,
        default=Decimal("12.3"),
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/valConstr"

    element_with_attr: Optional[ElementWithAttr] = field(
        default=None,
        metadata={
            "name": "elementWithAttr",
            "type": "Element",
            "required": True,
        }
    )
