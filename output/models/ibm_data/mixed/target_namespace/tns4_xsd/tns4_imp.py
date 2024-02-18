from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://test2"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "http://test2"

    value: Optional[int] = field(default=None)


@dataclass
class Y:
    class Meta:
        name = "y"
        namespace = "http://test2"

    a: List[A] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
