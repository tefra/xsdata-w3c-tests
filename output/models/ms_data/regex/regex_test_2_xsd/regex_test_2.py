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
            "pattern": r"(\p{Lu}\p{Ll}*)\s(\p{Lu}\p{Ll}*)",
        },
    )
