from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "foo"

    e1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    e2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
