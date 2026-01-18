from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a_or_b: None | Doc.A | Doc.B = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": ForwardRef("Doc.A"),
                },
                {
                    "name": "b",
                    "type": ForwardRef("Doc.B"),
                },
            ),
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
