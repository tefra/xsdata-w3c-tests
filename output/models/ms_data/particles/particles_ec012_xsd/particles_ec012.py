from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    a1_or_a2: None | Doc.A1 | Doc.A2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a1",
                    "type": ForwardRef("Doc.A1"),
                },
                {
                    "name": "a2",
                    "type": ForwardRef("Doc.A2"),
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class A1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )

    @dataclass(kw_only=True)
    class A2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )
