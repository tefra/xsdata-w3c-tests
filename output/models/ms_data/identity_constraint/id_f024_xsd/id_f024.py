from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class T:
    class Meta:
        name = "t"

    r: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "importNS",
        }
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    t: List[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
