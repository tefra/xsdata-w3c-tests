from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    choice: list[int | Foo.B | Foo.B2 | bool | Foo.D | object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": int,
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
                    "name": "c",
                    "type": bool,
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

    @dataclass(kw_only=True)
    class B:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class B2:
        value: str = field(default="")

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
class Doc(Foo):
    class Meta:
        name = "doc"
