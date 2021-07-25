from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    class Meta:
        name = "root"
        nillable = True

    e: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
        }
    )
