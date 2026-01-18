from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    b_or_b2: None | Foo.B | Foo.B2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b",
                    "type": ForwardRef("Foo.B"),
                    "namespace": "",
                },
                {
                    "name": "b2",
                    "type": ForwardRef("Foo.B2"),
                    "namespace": "",
                },
            ),
        },
    )
    w3_org_1999_xhtml_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "process_contents": "skip",
        },
    )
    c: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    a: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    d: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass(kw_only=True)
    class B:
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
class Doc(Foo):
    class Meta:
        name = "doc"
