from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class BCt:
    class Meta:
        name = "b-ct"

    c21_or_c22: list[BCt.C21 | BCt.C22] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c21",
                    "type": ForwardRef("BCt.C21"),
                    "namespace": "",
                    "max_occurs": 3,
                },
                {
                    "name": "c22",
                    "type": ForwardRef("BCt.C22"),
                    "namespace": "",
                    "max_occurs": 3,
                },
            ),
            "max_occurs": 3,
        },
    )

    @dataclass(kw_only=True)
    class C21:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class C22:
        value: int = field(
            metadata={
                "required": True,
            }
        )


@dataclass(kw_only=True)
class BE1(BCt):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"
