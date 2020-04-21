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
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
