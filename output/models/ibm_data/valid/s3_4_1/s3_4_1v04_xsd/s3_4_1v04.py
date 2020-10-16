from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class C:
    """
    :ivar x:
    :ivar y:
    :ivar any_element:
    """
    class Meta:
        name = "c"

    x: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    y: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar p:
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "a"

    p: Optional[C] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
