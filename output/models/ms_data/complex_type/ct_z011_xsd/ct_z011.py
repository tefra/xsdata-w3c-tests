from dataclasses import dataclass, field
from typing import Optional


@dataclass
class A:
    """
    :ivar any_element:
    """
    class Meta:
        name = "a"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class B:
    """
    :ivar any_element:
    """
    class Meta:
        name = "b"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
