from dataclasses import dataclass, field
from typing import List


@dataclass
class Foo:
    class Meta:
        name = "foo"

    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
