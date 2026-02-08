from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://foo.com"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    child1_or_child2: list[Root.Child1 | Root.Child2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "child1",
                    "type": ForwardRef("Root.Child1"),
                },
                {
                    "name": "child2",
                    "type": ForwardRef("Root.Child2"),
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Child1:
        value: list[str] = field(
            default_factory=list,
            metadata={
                "min_length": 5,
                "tokens": True,
            },
        )

    @dataclass(kw_only=True)
    class Child2:
        value: bool | str = field(
            default="",
            metadata={
                "min_length": 5,
            },
        )
