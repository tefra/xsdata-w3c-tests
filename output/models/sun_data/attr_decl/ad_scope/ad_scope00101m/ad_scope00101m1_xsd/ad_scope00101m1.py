from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "AttrDecl/scope"


@dataclass
class ElementWithAttr:
    """
    :ivar number:
    :ivar price:
    """
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrDecl/scope"

    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="AttrDecl/scope",
            required=True
        )
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/scope"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
