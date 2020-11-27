from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    ele: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
            "pattern": r"\i",
        }
    )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
