from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    value: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\P{Lu}+\p{Lu})\s(\P{Lu}+\p{Lu})",
        },
    )
