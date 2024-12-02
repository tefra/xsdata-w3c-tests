from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    w3_org_1999_xhtml_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "process_contents": "skip",
        },
    )
    d: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    b_or_b2: Optional[Union["Foo.B", "Foo.B2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b",
                    "type": ForwardRef("Foo.B"),
                    "namespace": "",
                },
                {
                    "name": "b2",
                    "type": ForwardRef("Foo.B2"),
                    "namespace": "",
                },
            ),
        },
    )
    a: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    c: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
class Doc(Foo):
    class Meta:
        name = "doc"
