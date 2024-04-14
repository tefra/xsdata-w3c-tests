from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    choice: Optional[
        Union[
            "Foo.One",
            "Foo.Two",
            "Foo.Three",
            "Foo.Four",
            "Foo.Five",
            "Foo.Five2",
            "Foo.Six",
            "Foo.Six2",
            "Foo.Seven",
            "Foo.Seven2",
            "Foo.Eight",
            "Foo.Eight2",
        ]
    ] = field(
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

    @dataclass
    class One:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Two:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Three:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Four:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Five:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Five2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Six:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Six2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Seven:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Seven2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Eight:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class Eight2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
