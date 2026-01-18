from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class B:
    e1_or_e2_or_e3: list[B.E1 | B.E2 | B.E3] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("B.E1"),
                    "namespace": "",
                    "max_occurs": 3,
                },
                {
                    "name": "e2",
                    "type": ForwardRef("B.E2"),
                    "namespace": "",
                    "max_occurs": 3,
                },
                {
                    "name": "e3",
                    "type": ForwardRef("B.E3"),
                    "namespace": "",
                    "max_occurs": 3,
                },
            ),
            "max_occurs": 3,
        },
    )

    @dataclass(kw_only=True)
    class E1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class E2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class E3:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class R:
    e3: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
