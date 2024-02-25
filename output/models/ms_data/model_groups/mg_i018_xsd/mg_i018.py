from dataclasses import dataclass, field
from typing import Optional, Type, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    choice: Optional[
        Union["Foo.S1", "Foo.S2", "Foo.S3", "Foo.S4", object]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "s1",
                    "type": Type["Foo.S1"],
                    "namespace": "",
                },
                {
                    "name": "s2",
                    "type": Type["Foo.S2"],
                    "namespace": "",
                },
                {
                    "name": "s3",
                    "type": Type["Foo.S3"],
                    "namespace": "",
                },
                {
                    "name": "s4",
                    "type": Type["Foo.S4"],
                    "namespace": "",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://n1 http://n2 http://n3 http://n4",
                },
            ),
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
