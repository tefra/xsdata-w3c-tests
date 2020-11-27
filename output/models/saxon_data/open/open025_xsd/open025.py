from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class T:
    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "required": True,
        }
    )
    i: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    d: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Doc(T):
    class Meta:
        name = "doc"
