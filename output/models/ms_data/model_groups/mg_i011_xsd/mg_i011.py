from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    choice: list[Union["Foo.B", "Foo.B2", bool, int, "Foo.D", object]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b",
                    "type": ForwardRef("Foo.B"),
                    "namespace": "",
                },
                {
                    "name": "b2",
                    "type": ForwardRef("Foo.B2"),
                    "namespace": "",
                },
                {
                    "name": "c",
                    "type": bool,
                    "namespace": "",
                },
                {
                    "name": "a",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "d",
                    "type": ForwardRef("Foo.D"),
                    "namespace": "",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class B:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class B2:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class D:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
