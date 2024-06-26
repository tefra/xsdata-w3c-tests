from dataclasses import dataclass, field
from typing import Optional, Union


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

    e1_or_e2: Optional[Union[str, Bar]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "e2",
                    "type": Bar,
                    "namespace": "",
                },
            ),
        },
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
