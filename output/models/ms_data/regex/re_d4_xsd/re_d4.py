from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*",
        },
    )
