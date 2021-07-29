from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    a2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
