from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"
        nillable = True

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 5,
        }
    )
    b: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 5,
        }
    )
    c: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
        }
    )
    d: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
