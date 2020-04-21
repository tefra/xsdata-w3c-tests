from dataclasses import dataclass, field
from typing import List


@dataclass
class C1:
    """
    :ivar e1:
    """
    e1: List["C1"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class Foo(C1):
    class Meta:
        name = "foo"
