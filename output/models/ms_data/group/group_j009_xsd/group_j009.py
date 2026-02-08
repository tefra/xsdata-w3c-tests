from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    b1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999,
        },
    )
    b2: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999,
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: Elem = field(
        metadata={
            "type": "Element",
        }
    )
