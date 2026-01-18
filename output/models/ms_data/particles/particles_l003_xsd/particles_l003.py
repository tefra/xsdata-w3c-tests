from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ForwardRef

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
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "c2",
                    "type": ForwardRef("B.C2"),
                    "namespace": "",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
    d1_or_d2: list[B.D1 | B.D2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "d1",
                    "type": ForwardRef("B.D1"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "d2",
                    "type": ForwardRef("B.D2"),
                    "namespace": "",
                    "max_occurs": 2,
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
    class D1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class D2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class R(B):
    c2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    d2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    c1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    d1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


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
