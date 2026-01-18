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
            "pattern": r"[0-9]+-[0-9]+-[0-9]+",
        },
    )


@dataclass(kw_only=True)
class Para2:
    class Meta:
        name = "para2"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]+-[0-9]+-[0-9]+",
        },
    )
