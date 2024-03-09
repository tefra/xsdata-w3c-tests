from dataclasses import dataclass, field
from typing import Any, Optional, Type, Union


@dataclass
class Bar:
    class Meta:
        name = "bar"

    e1_or_e2: Optional[Union["Bar.E1", "Bar.E2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": Type["Bar.E1"],
                    "namespace": "",
                },
                {
                    "name": "e2",
                    "type": Type["Bar.E2"],
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass
    class E1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class E2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )


@dataclass
class Foo(Bar):
    class Meta:
        name = "foo"

    e1: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
