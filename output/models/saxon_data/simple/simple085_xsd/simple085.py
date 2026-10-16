from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    value: str = field(
        metadata={
            "white_space": "collapse",
            "pattern": r"Hello world",
        }
    )
