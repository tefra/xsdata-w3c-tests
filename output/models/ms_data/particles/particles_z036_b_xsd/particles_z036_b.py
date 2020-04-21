from dataclasses import dataclass, field
from typing import List


@dataclass
class FooType:
    """
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "fooType"

    a: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=100000000
        )
    )
    b: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=100000
        )
    )


@dataclass
class Doc(FooType):
    class Meta:
        name = "doc"
