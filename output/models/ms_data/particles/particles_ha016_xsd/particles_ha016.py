from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo_or_bar: list[Doc.Foo | Doc.Bar] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": ForwardRef("Doc.Foo"),
                },
                {
                    "name": "bar",
                    "type": ForwardRef("Doc.Bar"),
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass(kw_only=True)
    class Foo:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )

    @dataclass(kw_only=True)
    class Bar:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )
