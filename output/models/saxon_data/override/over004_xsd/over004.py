from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Para:
    class Meta:
        name = "para"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[0-9]+-[0-9]+-[0-9]+",
        },
    )
