from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Elem:
    class Meta:
        name = "elem"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 100,
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: List[Elem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 100,
        },
    )
