from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    foo_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "foo",
            "max_occurs": 3,
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Doc(Base):
    class Meta:
        name = "doc"

    c1_or_c2: None | Doc.C1 | Doc.C2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": ForwardRef("Doc.C1"),
                },
                {
                    "name": "c2",
                    "type": ForwardRef("Doc.C2"),
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class C1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )

    @dataclass(kw_only=True)
    class C2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
            },
        )
