from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    choice: Optional[
        Union[
            "Foo.C1",
            "Foo.C2",
            "Foo.C3",
            "Foo.C4",
            "Foo.S1",
            "Foo.S2",
            "Foo.S3",
            "Foo.S4",
        ]
    ] = field(
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

    @dataclass
    class C1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class C2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class C3:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class C4:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class S1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class S2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class S3:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class S4:
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
