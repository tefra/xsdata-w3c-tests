from dataclasses import dataclass, field
from typing import List, Optional, Type, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    choice: List[Union[int, "Foo.B", "Foo.B2", bool, "Foo.D", object]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": Type["Foo.B"],
                    "namespace": "",
                },
                {
                    "name": "b2",
                    "type": Type["Foo.B2"],
                    "namespace": "",
                },
                {
                    "name": "c",
                    "type": bool,
                    "namespace": "",
                },
                {
                    "name": "d",
                    "type": Type["Foo.D"],
                    "namespace": "",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )

    @dataclass
    class B:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class B2:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class D:
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
