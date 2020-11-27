from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Beta:
    class Meta:
        name = "beta"


@dataclass
class Doc:
    class Meta:
        name = "doc"

    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    open_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
            "mixed": True,
        }
    )
