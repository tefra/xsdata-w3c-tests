from dataclasses import dataclass, field
from typing import List


@dataclass
class Foo:
    """
    :ivar e1:
    """
    class Meta:
        name = "foo"

    e1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
