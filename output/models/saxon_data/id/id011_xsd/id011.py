from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Para:
    class Meta:
        name = "para"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    id: str = field(
        init=False,
        default="para001",
        metadata={
            "type": "Attribute",
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
