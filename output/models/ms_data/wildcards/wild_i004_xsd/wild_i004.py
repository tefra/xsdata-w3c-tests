from dataclasses import dataclass, field
from typing import List


@dataclass
class Elt1:
    class Meta:
        name = "elt1"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Elt2:
    class Meta:
        name = "elt2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    elt1: List[Elt1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
