from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    choice: Optional[Union["Foo.E1", "Foo.E2", "Foo.E3", "Foo.E4", object]] = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "e1",
                        "type": ForwardRef("Foo.E1"),
                        "namespace": "",
                    },
                    {
                        "name": "e2",
                        "type": ForwardRef("Foo.E2"),
                        "namespace": "",
                    },
                    {
                        "name": "e3",
                        "type": ForwardRef("Foo.E3"),
                        "namespace": "",
                    },
                    {
                        "name": "e4",
                        "type": ForwardRef("Foo.E4"),
                        "namespace": "",
                    },
                    {
                        "wildcard": True,
                        "type": object,
                        "namespace": "http://n1 http://n2 http://n3 http://n4",
                        "max_occurs": 4,
                    },
                ),
            },
        )
    )

    @dataclass
    class E1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class E2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class E3:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class E4:
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
