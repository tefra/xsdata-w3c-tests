from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: list[bool | int | str] = field(
        init=False,
        default_factory=lambda: [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        ],
        metadata={
            "tokens": True,
        },
    )
