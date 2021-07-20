from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class C:
    class Meta:
        name = "c"

    a: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class D(C):
    class Meta:
        name = "d"
