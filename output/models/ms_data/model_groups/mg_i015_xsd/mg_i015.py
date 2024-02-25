from dataclasses import dataclass, field
from typing import Optional, Type, Union


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
                    "type": Type["Foo.One"],
                    "namespace": "",
                },
                {
                    "name": "two",
                    "type": Type["Foo.Two"],
                    "namespace": "",
                },
                {
                    "name": "three",
                    "type": Type["Foo.Three"],
                    "namespace": "",
                },
                {
                    "name": "four",
                    "type": Type["Foo.Four"],
                    "namespace": "",
                },
                {
                    "name": "five",
                    "type": Type["Foo.Five"],
                    "namespace": "",
                },
                {
                    "name": "five2",
                    "type": Type["Foo.Five2"],
                    "namespace": "",
                },
                {
                    "name": "six",
                    "type": Type["Foo.Six"],
                    "namespace": "",
                },
                {
                    "name": "six2",
                    "type": Type["Foo.Six2"],
                    "namespace": "",
                },
                {
                    "name": "seven",
                    "type": Type["Foo.Seven"],
                    "namespace": "",
                },
                {
                    "name": "seven2",
                    "type": Type["Foo.Seven2"],
                    "namespace": "",
                },
                {
                    "name": "eight",
                    "type": Type["Foo.Eight"],
                    "namespace": "",
                },
                {
                    "name": "eight2",
                    "type": Type["Foo.Eight2"],
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
