from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrGroup/attrUse"


@dataclass
class ElementWithAttr:
    """
    :ivar good:
    :ivar number:
    :ivar height:
    """
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrGroup/attrUse"

    good: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="AttrGroup/attrUse"
        )
    )
    height: Optional[Decimal] = field(
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
        namespace = "AttrGroup/attrUse"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )