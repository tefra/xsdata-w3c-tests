from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrUse/required"


@dataclass
class ElementWithAttr:
    """
    :ivar number:
    """
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrUse/required"

    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "AttrUse/required",
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "AttrUse/required"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
