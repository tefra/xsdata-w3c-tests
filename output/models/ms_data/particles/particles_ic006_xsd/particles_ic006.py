from dataclasses import dataclass, field
from typing import List


@dataclass
class Testing:
    class Meta:
        name = "testing"

    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
    e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
