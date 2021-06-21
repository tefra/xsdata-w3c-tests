from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Computer1:
    class Meta:
        name = "computer"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "max_occurs": 2,
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
class RestrictedComputer(Computer1):
    class Meta:
        name = "restrictedComputer"

    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "required": True,
        }
    )


@dataclass
class Computer(RestrictedComputer):
    class Meta:
        name = "computer"
