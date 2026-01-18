from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Example:
    value: list[int] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
