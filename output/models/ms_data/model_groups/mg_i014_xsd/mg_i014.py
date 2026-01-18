from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    choice: list[Foo.D | Foo.B | Foo.B2 | int | bool | object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "d",
                    "type": ForwardRef("Foo.D"),
                    "namespace": "",
                },
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
                    "name": "a",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "c",
                    "type": bool,
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

    @dataclass(kw_only=True)
    class D:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class B:
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class B2:
        value: str = field(
            metadata={
                "required": True,
            }
        )


@dataclass(kw_only=True)
class Doc(Foo):
    class Meta:
        name = "doc"
