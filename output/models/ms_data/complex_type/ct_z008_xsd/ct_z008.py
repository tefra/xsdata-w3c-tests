from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 4,
        }
    )
    b: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 4,
        }
    )
