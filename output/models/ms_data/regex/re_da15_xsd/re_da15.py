from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Regex:
    att: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(1|true|false|0|0)",
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
