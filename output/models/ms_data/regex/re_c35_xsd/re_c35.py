from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Regex:
    att: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"a*b{2,4}c{0}",
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
