from dataclasses import dataclass, field
from typing import Optional, Type, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    one: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    two: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    three: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    four: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    five_or_five2: Optional[Union["Foo.Five", "Foo.Five2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    six_or_six2: Optional[Union["Foo.Six", "Foo.Six2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    seven_or_seven2: Optional[Union["Foo.Seven", "Foo.Seven2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    eight_or_eight2: Optional[Union["Foo.Eight", "Foo.Eight2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
