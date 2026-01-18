from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    e1_or_e2: list[Elem.E1 | Elem.E2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("Elem.E1"),
                    "namespace": "",
                    "max_occurs": 3,
                },
                {
                    "name": "e2",
                    "type": ForwardRef("Elem.E2"),
                    "namespace": "",
                    "max_occurs": 3,
                },
            ),
            "min_occurs": 2,
            "max_occurs": 3,
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
class Doc:
    class Meta:
        name = "doc"

    elem: None | Elem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
