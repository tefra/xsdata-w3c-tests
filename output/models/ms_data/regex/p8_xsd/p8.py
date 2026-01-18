from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Regex:
    att: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": -9,
            "max_exclusive": 10,
            "pattern": r"\-[0-9]*",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: list[Regex] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
