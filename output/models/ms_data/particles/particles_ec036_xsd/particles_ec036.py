from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a_or_b: list[Doc.A | Doc.B] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": ForwardRef("Doc.A"),
                    "max_occurs": 4,
                },
                {
                    "name": "b",
                    "type": ForwardRef("Doc.B"),
                    "max_occurs": 4,
                },
            ),
            "max_occurs": 4,
        },
    )

    @dataclass(kw_only=True)
    class A:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )

    @dataclass(kw_only=True)
    class B:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )
