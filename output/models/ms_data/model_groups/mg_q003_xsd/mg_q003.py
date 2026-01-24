from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    e1_or_e2: list[Foo.E1 | Foo.E2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("Foo.E1"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "e2",
                    "type": ForwardRef("Foo.E2"),
                    "namespace": "",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 4,
        },
    )

    @dataclass(kw_only=True)
    class E1:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )

    @dataclass(kw_only=True)
    class E2:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )


@dataclass(kw_only=True)
class Doc(Foo):
    class Meta:
        name = "doc"
