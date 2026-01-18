from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    e1_or_e2: None | Foo.E1 | Foo.E2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("Foo.E1"),
                    "namespace": "",
                },
                {
                    "name": "e2",
                    "type": ForwardRef("Foo.E2"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class E1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class E2:
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
