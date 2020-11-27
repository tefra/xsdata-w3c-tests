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
        }
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"

    e1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    e2: Optional[Bar] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
