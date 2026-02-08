from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class NewSize:
    class Meta:
        name = "newSize"

    value: int = field(
        metadata={
            "max_inclusive": 16,
        }
    )
