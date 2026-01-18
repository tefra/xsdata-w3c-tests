from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    a_or_b: None | Test.A | Test.B = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": ForwardRef("Test.A"),
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": ForwardRef("Test.B"),
                    "namespace": "",
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
class Root(Test):
    class Meta:
        name = "root"
