from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    a_or_b: list[FooType.A | FooType.B] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": ForwardRef("FooType.A"),
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": ForwardRef("FooType.B"),
                    "namespace": "",
                    "max_occurs": 100000,
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class A:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class B:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class Doc(FooType):
    class Meta:
        name = "doc"
