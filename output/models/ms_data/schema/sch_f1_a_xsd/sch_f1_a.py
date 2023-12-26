from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class CtA:
    class Meta:
        name = "ct-A"

    a1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        },
    )
    a2: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class E1(CtA):
    class Meta:
        name = "e1"
        namespace = "ns-a"
