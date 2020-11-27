from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


@dataclass
class C:
    class Meta:
        name = "c"

    a: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
    b: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )


@dataclass
class Root(C):
    class Meta:
        name = "root"
        namespace = "a"
