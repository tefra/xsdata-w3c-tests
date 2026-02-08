from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class ACt:
    class Meta:
        name = "a-ct"

    c21_or_c22: list[ACt.C21 | ACt.C22] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c21",
                    "type": ForwardRef("ACt.C21"),
                    "namespace": "",
                    "max_occurs": 3,
                },
                {
                    "name": "c22",
                    "type": ForwardRef("ACt.C22"),
                    "namespace": "",
                    "max_occurs": 3,
                },
            ),
            "max_occurs": 3,
        },
    )

    @dataclass(kw_only=True)
    class C21:
        value: int = field()

    @dataclass(kw_only=True)
    class C22:
        value: int = field()


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
class E1(ACt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
