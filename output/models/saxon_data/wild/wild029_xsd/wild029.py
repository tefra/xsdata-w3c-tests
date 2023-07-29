from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Eden:
    class Meta:
        name = "eden"

    a: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 3,
            "max_occurs": 3,
            "sequence": 1,
        }
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        }
    )
