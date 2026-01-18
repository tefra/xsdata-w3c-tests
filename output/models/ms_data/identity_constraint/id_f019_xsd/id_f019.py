from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    col: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    row: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    t: list[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
