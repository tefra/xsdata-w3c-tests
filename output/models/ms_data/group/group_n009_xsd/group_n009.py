from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    a1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999999,
            "sequence": 1,
        },
    )
    a2: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999999,
            "sequence": 1,
        },
    )
    a3: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999999,
            "sequence": 1,
        },
    )
    a4: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999999,
            "sequence": 1,
        },
    )
    a5: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 99999999999999,
            "sequence": 1,
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
