from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class N:
    class Meta:
        name = "n"

    value: str = field(default="")


@dataclass(kw_only=True)
class Outer:
    class Meta:
        name = "outer"

    n: list[N] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
