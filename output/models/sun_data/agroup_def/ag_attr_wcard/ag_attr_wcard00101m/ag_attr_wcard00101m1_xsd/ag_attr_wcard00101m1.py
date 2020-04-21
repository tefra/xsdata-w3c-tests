from decimal import Decimal
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional

__NAMESPACE__ = "AttrGroup/attrWCard"


@dataclass
class ElementWithAttr:
    """
    :ivar good:
    :ivar number:
    :ivar height:
    :ivar any_attributes:
    """
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrGroup/attrWCard"

    good: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "AttrGroup/attrWCard"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
