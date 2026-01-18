from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
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
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class B2:
        value: str = field(
            metadata={
                "required": True,
            }
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
