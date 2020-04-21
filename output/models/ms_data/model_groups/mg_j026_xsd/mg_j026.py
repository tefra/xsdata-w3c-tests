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
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
