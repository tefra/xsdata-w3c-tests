from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class B:
    x: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Elem(B):
    class Meta:
        name = "elem"

    a1_or_a2: list[Elem.A1 | Elem.A2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "A1",
                    "type": ForwardRef("Elem.A1"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "A2",
                    "type": ForwardRef("Elem.A2"),
                    "namespace": "",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass(kw_only=True)
    class A1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class A2:
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
            "required": True,
        }
    )
