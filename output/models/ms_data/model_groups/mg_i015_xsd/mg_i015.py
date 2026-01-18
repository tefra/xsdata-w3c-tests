from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    choice: (
        None
        | Foo.One
        | Foo.Two
        | Foo.Three
        | Foo.Four
        | Foo.Five
        | Foo.Five2
        | Foo.Six
        | Foo.Six2
        | Foo.Seven
        | Foo.Seven2
        | Foo.Eight
        | Foo.Eight2
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "one",
                    "type": ForwardRef("Foo.One"),
                    "namespace": "",
                },
                {
                    "name": "two",
                    "type": ForwardRef("Foo.Two"),
                    "namespace": "",
                },
                {
                    "name": "three",
                    "type": ForwardRef("Foo.Three"),
                    "namespace": "",
                },
                {
                    "name": "four",
                    "type": ForwardRef("Foo.Four"),
                    "namespace": "",
                },
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
    class One:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Two:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Three:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class Four:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
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
