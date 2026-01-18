from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Temp:
    class Meta:
        name = "temp"

    value: str = field(
        default="",
        metadata={
            "pattern": r"2008.*",
        },
    )
