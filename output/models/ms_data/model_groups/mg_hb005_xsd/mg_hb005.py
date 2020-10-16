from dataclasses import dataclass, field
from typing import List


@dataclass
class Foo:
    """
    :ivar t1:
    """
    class Meta:
        name = "foo"

    t1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 5,
        }
    )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
