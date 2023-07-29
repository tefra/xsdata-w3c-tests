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
            "process_contents": "skip",
        }
    )
    extra_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://extra.com/",
            "max_occurs": 2,
            "process_contents": "skip",
        }
    )


@dataclass
class RestrictedComputer(Computer1):
    class Meta:
        name = "restrictedComputer"


@dataclass
class Computer(RestrictedComputer):
    class Meta:
        name = "computer"
