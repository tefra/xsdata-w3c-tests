from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e5: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e6: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
