from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"

    a: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        },
    )
    b: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    c: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
        },
    )
    d: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class E(B):
    class Meta:
        name = "e"

    e: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    f: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 3,
            "max_occurs": 4,
        },
    )
    g: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 4,
        },
    )


@dataclass(kw_only=True)
class Doc(E):
    class Meta:
        name = "doc"
