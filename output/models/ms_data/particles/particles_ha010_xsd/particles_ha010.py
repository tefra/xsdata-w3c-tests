from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    x_or_y: list[Doc.X | Doc.Y] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "x",
                    "type": ForwardRef("Doc.X"),
                },
                {
                    "name": "y",
                    "type": ForwardRef("Doc.Y"),
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass(kw_only=True)
    class X:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )

    @dataclass(kw_only=True)
    class Y:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )
