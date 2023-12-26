from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CtA:
    class Meta:
        name = "ct-A"

    a1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    a2: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

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
