from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/targetNS"


@dataclass
class ElementWithAttr:
    """
    :ivar number:
    :ivar price:
    """
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/targetNS"

    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="AttrDecl/targetNS"
        )
    )


@dataclass
class Root:
    """
    :ivar element_with_attr:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/targetNS"

    element_with_attr: Optional[ElementWithAttr] = field(
        default=None,
        metadata=dict(
            name="elementWithAttr",
            type="Element",
            required=True
        )
    )