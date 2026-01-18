from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    e1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    f1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    f2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c1_or_c2: None | Foo.C1 | Foo.C2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": ForwardRef("Foo.C1"),
                    "namespace": "",
                },
                {
                    "name": "c2",
                    "type": ForwardRef("Foo.C2"),
                    "namespace": "",
                },
            ),
        },
    )
    d1_or_d2: None | Foo.D1 | Foo.D2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "d1",
                    "type": ForwardRef("Foo.D1"),
                    "namespace": "",
                },
                {
                    "name": "d2",
                    "type": ForwardRef("Foo.D2"),
                    "namespace": "",
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
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class C2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class D1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class D2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class Doc(Foo):
    class Meta:
        name = "doc"
