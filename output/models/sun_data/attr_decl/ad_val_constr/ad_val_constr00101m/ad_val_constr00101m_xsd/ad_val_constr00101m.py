from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/valConstr"


@dataclass
class ElementWithAttr:
    """
    :ivar number:
    :ivar price:
    """
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/valConstr"

    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="AttrDecl/valConstr"
        )
    )
    price: Decimal = field(
        init=False,
        default=Decimal('12.3'),
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar element_with_attr:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/valConstr"

    element_with_attr: Optional[ElementWithAttr] = field(
        default=None,
        metadata=dict(
            name="elementWithAttr",
            type="Element",
            required=True
        )
    )
