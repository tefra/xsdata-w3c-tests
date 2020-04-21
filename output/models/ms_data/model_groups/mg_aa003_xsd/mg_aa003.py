from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar t1:
    """
    class Meta:
        name = "foo"

    t1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
