from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "foo"

    a: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: Optional[object] = field(
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
