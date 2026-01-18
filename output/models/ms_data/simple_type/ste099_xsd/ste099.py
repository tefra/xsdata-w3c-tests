from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: list[str] = field(
        init=False,
        default_factory=lambda: [
            "abcdefab",
        ],
        metadata={
            "tokens": True,
        },
    )
