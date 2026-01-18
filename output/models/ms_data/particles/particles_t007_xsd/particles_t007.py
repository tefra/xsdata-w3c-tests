from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    c1_or_c2_or_c3: list[B.C1 | B.C2 | B.C3] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": ForwardRef("B.C1"),
                    "namespace": "",
                },
                {
                    "name": "c2",
                    "type": ForwardRef("B.C2"),
                    "namespace": "",
                },
                {
                    "name": "c3",
                    "type": ForwardRef("B.C3"),
                    "namespace": "",
                },
            ),
        },
    )
    foo: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass(kw_only=True)
    class C1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class C2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class C3:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class R(B):
    pass


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: None | R = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
