from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar a:
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


@dataclass
class Bar(Foo):
    """
    :ivar b:
    """
    class Meta:
        name = "bar"

    b: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
