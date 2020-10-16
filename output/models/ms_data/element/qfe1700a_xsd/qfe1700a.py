from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E2:
    """
    :ivar e3:
    """
    class Meta:
        name = "e2"
        nillable = True

    e3: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar e1:
    :ivar any_element:
    """
    class Meta:
        name = "root"

    e1: Optional[str] = field(
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
