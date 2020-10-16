from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "AttrGroup/name"


@dataclass
class ElementWithAttr:
    """
    :ivar good:
    :ivar number:
    :ivar height:
    """
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrGroup/name"

    good: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "AttrGroup/name"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
