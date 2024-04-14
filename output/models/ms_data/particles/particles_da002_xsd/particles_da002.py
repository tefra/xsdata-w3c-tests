from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class A:
    a1_or_a2: Optional[Union["A.A1", "A.A2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a1",
                    "type": ForwardRef("A.A1"),
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "a2",
                    "type": ForwardRef("A.A2"),
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )

    @dataclass
    class A1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )

    @dataclass
    class A2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    elem2: Optional[A] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
