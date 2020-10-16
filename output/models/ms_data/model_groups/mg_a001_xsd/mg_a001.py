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
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
