from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/type"


@dataclass
class ElementWithAttr:
    """
    :ivar number:
    :ivar price:
    """
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/type"

    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="AttrDecl/type",
            min_exclusive=0.0,
            max_exclusive=13.0
        )
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            min_exclusive=0.0,
            max_exclusive=13.0
        )
    )


@dataclass
class Root:
    """
    :ivar element_with_attr:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/type"

    element_with_attr: Optional[ElementWithAttr] = field(
        default=None,
        metadata=dict(
            name="elementWithAttr",
            type="Element",
            required=True
        )
    )
