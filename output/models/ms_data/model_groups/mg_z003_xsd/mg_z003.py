from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bar:
    class Meta:
        name = "bar"


@dataclass
class Foo(Bar):
    """
    :ivar e1:
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


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
