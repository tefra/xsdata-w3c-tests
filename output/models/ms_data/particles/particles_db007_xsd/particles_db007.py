from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class A:
    a1_or_a2: None | A.A1 | A.A2 = field(
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

    @dataclass(kw_only=True)
    class A1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )

    @dataclass(kw_only=True)
    class A2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )


@dataclass(kw_only=True)
class Elem1:
    class Meta:
        name = "elem1"
        namespace = "http://xsdtesting"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Elem2(A):
    class Meta:
        name = "elem2"
        namespace = "http://xsdtesting"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem1: Elem1 = field(
        metadata={
            "type": "Element",
        }
    )
    elem2: Elem2 = field(
        metadata={
            "type": "Element",
        }
    )
