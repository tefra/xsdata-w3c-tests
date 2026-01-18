from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    att: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
