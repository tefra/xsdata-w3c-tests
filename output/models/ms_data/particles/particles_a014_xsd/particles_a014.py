from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elem:
    class Meta:
        name = "elem"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "min_occurs": 2,
            "max_occurs": 1000000,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
