from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class List:
    class Meta:
        name = "list"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Outer:
    class Meta:
        name = "outer"

    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "min_occurs": 1,
        },
    )
