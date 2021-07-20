from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    class Meta:
        name = "root"

    r: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 10,
            "pattern": r"\Dx",
        }
    )
