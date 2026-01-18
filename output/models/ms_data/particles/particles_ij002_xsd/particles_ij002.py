from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    f1_or_f2: list[Foo.F1 | Foo.F2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "f1",
                    "type": ForwardRef("Foo.F1"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 100,
                },
                {
                    "name": "f2",
                    "type": ForwardRef("Foo.F2"),
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 100,
        },
    )

    @dataclass(kw_only=True)
    class F1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )

    @dataclass(kw_only=True)
    class F2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )


@dataclass(kw_only=True)
class B:
    c1_or_c2: None | Foo | object = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": Foo,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "c2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class R(B):
    pass


@dataclass(kw_only=True)
class Elem(R):
    class Meta:
        name = "elem"
        namespace = "http://xsdtesting"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | Elem = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
