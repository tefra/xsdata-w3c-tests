from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "urn:test"


@dataclass(kw_only=True)
class Root:
    class Meta:
        namespace = "urn:test"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "A",
                    "type": ForwardRef("Root.A"),
                },
                {
                    "name": "B1",
                    "type": ForwardRef("Root.B1"),
                },
                {
                    "name": "B2",
                    "type": ForwardRef("Root.B2"),
                },
                {
                    "name": "B3",
                    "type": ForwardRef("Root.B3"),
                },
                {
                    "name": "B4",
                    "type": ForwardRef("Root.B4"),
                },
                {
                    "name": "B5",
                    "type": ForwardRef("Root.B5"),
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class A:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class B1:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class B2:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class B3:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class B4:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class B5:
        value: str = field(default="")
