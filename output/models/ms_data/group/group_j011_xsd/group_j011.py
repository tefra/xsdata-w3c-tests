from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    choice: None | Elem.B1 | Elem.B2 | Elem.B3 | Elem.B4 = field(
        default=None,
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
                {
                    "name": "b3",
                    "type": ForwardRef("Elem.B3"),
                    "namespace": "",
                },
                {
                    "name": "b4",
                    "type": ForwardRef("Elem.B4"),
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
    class B3:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class B4:
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
