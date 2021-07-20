from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    class Meta:
        name = "root"

    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 10,
        }
    )
    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 10,
        }
    )
