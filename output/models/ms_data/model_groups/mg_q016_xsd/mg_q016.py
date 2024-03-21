from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bar:
    class Meta:
        name = "bar"

    e1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"

    e1_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "e1",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    e1: Optional[str] = field(
        default=None,
        metadata={
            "wrapper": "e2",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
