from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class RestrictedComputer:
    """
    :ivar name:
    :ivar local_element:
    :ivar extra_com_element:
    """
    class Meta:
        name = "restrictedComputer"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "required": True,
        }
    )
    extra_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://extra.com/",
            "max_occurs": 2,
        }
    )


@dataclass
class Computer(RestrictedComputer):
    class Meta:
        name = "computer"
