from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ns-a"


@dataclass
class E1:
    class Meta:
        name = "e1"
        namespace = "ns-a"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 4,
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
