from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    class Meta:
        name = "doc"
        nillable = True

    a_ns_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://a.ns/",
            "mixed": True,
            "min_occurs": 2,
            "max_occurs": 5,
        }
    )
    b_ns_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://b.ns/",
        }
    )
