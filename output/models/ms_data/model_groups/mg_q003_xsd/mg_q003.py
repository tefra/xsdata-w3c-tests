from dataclasses import dataclass, field
from typing import List


@dataclass
class Foo:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "foo"

    e1: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    e2: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequential": True,
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
