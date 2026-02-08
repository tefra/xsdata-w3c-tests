from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    b1_or_b2: list[Elem.B1 | Elem.B2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b1",
                    "type": ForwardRef("Elem.B1"),
                    "namespace": "",
                },
                {
                    "name": "b2",
                    "type": ForwardRef("Elem.B2"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class B1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class B2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: Elem = field(
        metadata={
            "type": "Element",
        }
    )
