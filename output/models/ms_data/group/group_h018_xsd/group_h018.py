from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class A:
    choice: list[A.X1 | A.X2 | A.Y1 | A.Y2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "x1",
                    "type": ForwardRef("A.X1"),
                    "namespace": "",
                    "max_occurs": 3,
                },
                {
                    "name": "x2",
                    "type": ForwardRef("A.X2"),
                    "namespace": "",
                    "max_occurs": 3,
                },
                {
                    "name": "y1",
                    "type": ForwardRef("A.Y1"),
                    "namespace": "",
                },
                {
                    "name": "y2",
                    "type": ForwardRef("A.Y2"),
                    "namespace": "",
                },
            ),
            "max_occurs": 6,
        },
    )

    @dataclass(kw_only=True)
    class X1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class X2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Y1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Y2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class Elem(A):
    class Meta:
        name = "elem"


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
