from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Message:
    class Meta:
        name = "message"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 25,
        },
    )
