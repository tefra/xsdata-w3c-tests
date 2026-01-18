from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: str = field(
        default="abc",
        metadata={
            "required": True,
        },
    )
