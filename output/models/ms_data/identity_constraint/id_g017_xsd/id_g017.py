from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class T:
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"

    row: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    col: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t: List[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
