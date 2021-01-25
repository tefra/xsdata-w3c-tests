from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class B:
    open_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
        }
    )


@dataclass
class R(B):
    open_com_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
            "required": True,
        }
    )


@dataclass
class Doc(R):
    class Meta:
        name = "doc"
