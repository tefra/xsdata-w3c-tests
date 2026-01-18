from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class E:
    class Meta:
        name = "e"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[a-zA-[pqr]]*",
        },
    )
