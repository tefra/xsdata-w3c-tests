from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class BCt:
    class Meta:
        name = "b-ct"

    b1_or_b2: None | BCt.B1 | BCt.B2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b1",
                    "type": ForwardRef("BCt.B1"),
                    "namespace": "ns-a",
                },
                {
                    "name": "b2",
                    "type": ForwardRef("BCt.B2"),
                    "namespace": "ns-a",
                },
            ),
        },
    )
    b3_or_b4: None | BCt.B3 | BCt.B4 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b3",
                    "type": ForwardRef("BCt.B3"),
                    "namespace": "ns-a",
                },
                {
                    "name": "b4",
                    "type": ForwardRef("BCt.B4"),
                    "namespace": "ns-a",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class B1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "ns-a",
            },
        )

    @dataclass(kw_only=True)
    class B2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "ns-a",
            },
        )

    @dataclass(kw_only=True)
    class B3:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "ns-a",
            },
        )

    @dataclass(kw_only=True)
    class B4:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "ns-a",
            },
        )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class E1(BCt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
