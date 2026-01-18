from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ForwardRef


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"

    e1_or_e2: None | Bar.E1 | Bar.E2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("Bar.E1"),
                    "namespace": "",
                },
                {
                    "name": "e2",
                    "type": ForwardRef("Bar.E2"),
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
class Foo(Bar):
    class Meta:
        name = "foo"

    e1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Doc(Foo):
    class Meta:
        name = "doc"
