from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    one: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    two: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    three: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    four: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    five_or_five2: None | Foo.Five | Foo.Five2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "five",
                    "type": ForwardRef("Foo.Five"),
                    "namespace": "",
                },
                {
                    "name": "five2",
                    "type": ForwardRef("Foo.Five2"),
                    "namespace": "",
                },
            ),
        },
    )
    six_or_six2: None | Foo.Six | Foo.Six2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "six",
                    "type": ForwardRef("Foo.Six"),
                    "namespace": "",
                },
                {
                    "name": "six2",
                    "type": ForwardRef("Foo.Six2"),
                    "namespace": "",
                },
            ),
        },
    )
    seven_or_seven2: None | Foo.Seven | Foo.Seven2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "seven",
                    "type": ForwardRef("Foo.Seven"),
                    "namespace": "",
                },
                {
                    "name": "seven2",
                    "type": ForwardRef("Foo.Seven2"),
                    "namespace": "",
                },
            ),
        },
    )
    eight_or_eight2: None | Foo.Eight | Foo.Eight2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "eight",
                    "type": ForwardRef("Foo.Eight"),
                    "namespace": "",
                },
                {
                    "name": "eight2",
                    "type": ForwardRef("Foo.Eight2"),
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Five:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Five2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Six:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Six2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Seven:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Seven2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Eight:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Eight2:
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
