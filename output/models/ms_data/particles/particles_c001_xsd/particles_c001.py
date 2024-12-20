from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Elem:
    class Meta:
        name = "elem"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: list[Elem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 100,
        },
    )
