from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar content:
    """
    class Meta:
        name = "fooType"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
