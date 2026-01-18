from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    choice: list[Elem.E1 | Elem.E2 | Elem.E3 | Elem.E4] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("Elem.E1"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "e2",
                    "type": ForwardRef("Elem.E2"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "e3",
                    "type": ForwardRef("Elem.E3"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "e4",
                    "type": ForwardRef("Elem.E4"),
                    "namespace": "",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
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
    class E3:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class E4:
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
