from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Para:
    class Meta:
        name = "para"

    value: str = field(default="")
    key: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    ref: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
