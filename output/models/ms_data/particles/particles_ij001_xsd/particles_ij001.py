from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    c1_or_c2: list[B.C1 | B.C2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": ForwardRef("B.C1"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 2,
                },
                {
                    "name": "c2",
                    "type": ForwardRef("B.C2"),
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass(kw_only=True)
    class C1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
            },
        )

    @dataclass(kw_only=True)
    class C2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
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
