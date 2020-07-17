from dataclasses import dataclass, field
from typing import List


@dataclass
class FooType:
    """
    :ivar content:
    """
    class Meta:
        name = "fooType"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
