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
        metadata={
            "type": "Element",
            "namespace": "",
        }
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
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Root(Bar):
    class Meta:
        name = "root"
