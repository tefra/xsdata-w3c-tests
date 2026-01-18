from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    choice: (
        None
        | Foo.C1
        | Foo.C2
        | Foo.C3
        | Foo.C4
        | Foo.S1
        | Foo.S2
        | Foo.S3
        | Foo.S4
    ) = field(
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
                {
                    "name": "c3",
                    "type": ForwardRef("Foo.C3"),
                    "namespace": "",
                },
                {
                    "name": "c4",
                    "type": ForwardRef("Foo.C4"),
                    "namespace": "",
                },
                {
                    "name": "s1",
                    "type": ForwardRef("Foo.S1"),
                    "namespace": "",
                },
                {
                    "name": "s2",
                    "type": ForwardRef("Foo.S2"),
                    "namespace": "",
                },
                {
                    "name": "s3",
                    "type": ForwardRef("Foo.S3"),
                    "namespace": "",
                },
                {
                    "name": "s4",
                    "type": ForwardRef("Foo.S4"),
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
    class C3:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class C4:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class S1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class S2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class S3:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class S4:
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
